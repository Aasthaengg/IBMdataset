N = int(input())
G = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
c = list(map(int,input().split()))
c.sort()
ans = sum(c) - max(c)
F = []
for i in range(1,N+1):
    n = len(G[i])
    if n == 1:
        F.append(i)
d = {}
i = 0
while i < N:
    x = F.pop(0)
    d[x] = c[i]
    i += 1
    if len(G[x]) > 0:
        y = G[x][0]
        G[y].remove(x)
        if len(G[y]) == 1:
            F.append(y)
ANS = []
for i in range(1,N+1):
    ANS.append(d[i])
print(ans)
print(*ANS)