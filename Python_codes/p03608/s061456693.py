import itertools
def warshall_floyd(g):
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                g[i][j] = min(g[i][j], g[i][k]+g[k][j])
    return g

n,m,r = map(int,input().split())
lst = list(map(int,input().split()))
graph = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
for i in range(n):
    graph[i][i] = 0
d = warshall_floyd(graph)

res = float('inf')
for l in itertools.permutations(lst):
    cnt = 0
    for i in range(1, len(l)):
        cnt += d[l[i-1]-1][l[i]-1]
    res = min(res, cnt)
print(res)