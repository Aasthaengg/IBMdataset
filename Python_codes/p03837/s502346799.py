# -*- coding: utf-8 -*-
N, M = map(int, input().split(' '))
graph = [[float('inf') for _ in range(N)] for _ in range(N)]

edges = [list(map(int, input().split(' '))) for _ in range(M)]
for a, b, c in edges:
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c


for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for a, b, c in edges:
    a -= 1
    b -= 1
    if graph[a][b] < c:
        ans += 1

print(ans)

