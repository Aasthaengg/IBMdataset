N = int(input())
AB = [list(map(int,input().split())) for _ in [0]*(N-1)]
*C, = sorted(map(int,input().split()))
print(sum(C[:-1]))
E = [[] for _ in [0]*N]
d = [0]*N
for a,b in AB:
    E[a-1].append(b-1)
    E[b-1].append(a-1)

for i in range(N):
    if len(E[i])>1:break
q = [i]
while q:
    i = q.pop()
    d[i] = C.pop()
    for j in E[i]:
        if d[j] != 0:continue
        q.append(j)
print(*d)