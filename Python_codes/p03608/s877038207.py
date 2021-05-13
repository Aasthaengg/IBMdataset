#%%
import itertools

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

n, m, R = map(int, input().split())
r = list(map(lambda x: int(x)-1,input().split()))
dist = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    dist[a][b] = c
    dist[b][a] = c
dist = warshall_floyd(dist)

l = list(itertools.permutations(r))
ans = float("inf")
for i in range(len(l)):
    tmp = 0
    for j in range(len(r)-1):
        tmp += dist[l[i][j]][l[i][j+1]]
    ans = min(ans, tmp)
print(ans)