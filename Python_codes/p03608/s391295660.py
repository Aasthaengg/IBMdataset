n, m, r = map(int, input().split())  # n:頂点数　w:辺の数
r_list = list(map(int, input().split()))
graph = [[float('inf')]*n for i in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w
for i in range(n):
    graph[i][i] = 0

def warshall_floyd(d):
    # d[i][j] : i から j への最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d


from itertools import permutations

adj_m=warshall_floyd(graph)
ans=float('inf')
for path in permutations(r_list):
    tmp_dist=0
    for i in range(r-1):
        tmp_dist+=adj_m[path[i]-1][path[i+1]-1]
    ans=min(ans, tmp_dist)
print(ans)
