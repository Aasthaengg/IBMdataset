import math

N, M, L = list(map(int, input().split()))
graph = [[math.inf]*N for _ in range(N)]

for i in range(M):
    a, b, c = list(map(int, input().split()))
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

Q = int(input())
query = [(0, 0) for _ in range(Q)]

for i in range(Q):
    query[i] = tuple(map(int, input().split()))

# Warshall-Floyd
for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

fuel_cost = [[math.inf]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] <= L:
            fuel_cost[i][j] = 1

# Warshall-Floyd
for i in range(N):
    for j in range(N):
        for k in range(N):
            fuel_cost[j][k] = min(fuel_cost[j][k], fuel_cost[j][i] + fuel_cost[i][k])

for i in range(Q):
    if fuel_cost[query[i][0] - 1][query[i][1] - 1] == math.inf:
        print(-1)
    else:
        print(fuel_cost[query[i][0] - 1][query[i][1] - 1] - 1)