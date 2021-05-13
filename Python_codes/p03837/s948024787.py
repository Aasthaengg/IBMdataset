import sys
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
n, m = [int(i) for i in sys.stdin.readline().split()]
graph = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b, c = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c
new_graph = csgraph_from_dense(graph)
res = floyd_warshall(new_graph)
cnt = 0
for i in range(n):
    for j in range(i, n):
        if graph[i][j] > 0 and graph[i][j] != res[i][j]:
            cnt += 1
print(cnt)