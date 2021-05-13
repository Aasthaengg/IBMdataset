from itertools import permutations


n, m, r = map(int, input().split())
towns = list(map(int, input().split()))

INF = float('inf')

graph = [[INF for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c

# ワーシャルフロイド

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_dist = 10**10
for route in permutations(towns, r):
    dist = 0
    for i in range(r-1):
        a = route[i] - 1
        b = route[i+1] - 1
        dist += graph[a][b]
    if dist < min_dist:
        min_dist = dist

print(min_dist)
