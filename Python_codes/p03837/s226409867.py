import sys
from scipy.sparse.csgraph import dijkstra

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[0 if i == j else float("inf") for i in range(N)] for j in range(N)]
for i in range(M):
    ai, bi, ci = map(int, input().split())
    graph[ai - 1][bi - 1] = ci
    graph[bi - 1][ai - 1] = ci

dist = dijkstra(graph, directed=False)

cnt = 0
for i in range(N):
    for j in range(N):
        used = False
        if i > j:
            continue
        for k in range(N):
            if graph[i][j] + dist[k][i] == dist[i][j]:
                used = True
                break
        if not used and graph[i][j] != float("inf"):
            cnt += 1
print(cnt)
