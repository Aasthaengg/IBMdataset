from scipy.sparse.csgraph import csgraph_from_dense, dijkstra

n,m = map(int,input().split())
edges = [[int(x) for x in input().split()] for i in range(m)]
graph = [[False]*n for i in range(n)]
for a, b, c in edges :
    graph[a-1][b-1] = c

graph = csgraph_from_dense(graph)
dist = dijkstra(graph, directed=False).astype(int)

ans = 0
for a, b, c in edges :
    if dist[a-1][b-1] != c :
        ans += 1

print(ans)
