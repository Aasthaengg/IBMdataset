from copy import deepcopy
N, M = map(int, input().split())
INF = 10**9+7
graph = [[INF for _ in range(N)] for l in range(N)]

for i in range(M):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1

  graph[b][a] = c
  graph[a][b] = c

newGraph = deepcopy(graph)

for k in range(N):
  for i in range(N):
    for j in range(N):
      newGraph[i][j] = min(newGraph[i][j], newGraph[i][k] + newGraph[k][j])

res = 0
for (i, row) in enumerate(newGraph):
  for (j, weight) in enumerate(row):
    if graph[i][j] != weight and graph[i][j] != INF:
      res += 1
print(res//2)