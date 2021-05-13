n,m,r = map(int, input().split())
INF = 1 << 40
edges = [[INF]*n for i in range(n)]
rs  = list(map(int, input().split()))
rs = [r-1 for r in rs]
for i in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a][b] = c
    edges[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            tmp = edges[i][k] + edges[k][j]
            edges[i][j] = min(edges[i][j], tmp)

from itertools import permutations

ans = 1 << 50
for perm in permutations(rs):
    dist = 0
    for i in range(1,len(perm)):
        f = perm[i-1]
        t = perm[i]
        dist += edges[f][t]
    ans = min(ans, dist)
print(ans)