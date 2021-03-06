N, M = map(int, input().split())

to = [[] for i in range(100010)]

for i in range(M):
    a, b = map(int, input().split())
    to[a].append(b)
    to[b].append(a)

dist = [0] * (N+1)
q = [1]
dist[0] = -1
#print(to[:4])

dist = [0] * N
pre = [0] * N

while len(q) != 0:
    a = q.pop(0)
    for i in to[a]:
        if dist[i-1] == 0:
            dist[i-1] = dist[a-1] + 1
            pre[i-1] = a
            q.append(i)
    #print(q)

print("Yes")
for i in range(1, N):
    print(pre[i])
