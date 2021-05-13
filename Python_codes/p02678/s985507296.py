import collections

N, M = map(int, input().split())
AB = []
for m in range(M):
    a, b = map(int, input().split())
    AB.append((a, b))

Cost = [[] for l in range(N+1)]
R = [0]*(N+1)
#print(Cost)

for a, b in AB:
    Cost[a].append(b)
    Cost[b].append(a)

#print(AB)
#print(Cost)

Rcount = 0
Pipod = collections.deque()
Pipod.append(1)
while Rcount != N-1:
    #print(Pipod)
    p = Pipod.popleft()
    #print(Cost[p])
    for c in Cost[p]:
        if c != 1 and R[c] == 0:
            R[c] = p
            Pipod.append(c)
            Rcount += 1
    if len(Pipod) == 0:
        print('No')
        exit(0)

print('Yes')
for x in R[2:N+1]:
    print(x)