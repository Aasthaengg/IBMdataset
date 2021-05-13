from copy import deepcopy
N, M = map(int, input().split())

graph = [[float('infinity')] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
ans = 0
# 頂点g -> eまでの最短経路コストと、その経路を記録する

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

original = deepcopy(graph)

def warshall_floyd(graph, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

warshall_floyd(graph, N)

ans = 0
for i in range(N):
    for j in range(i):
        if original[i][j] != float('infinity') and graph[i][j] != original[i][j]:
            ans += 1
print(ans)