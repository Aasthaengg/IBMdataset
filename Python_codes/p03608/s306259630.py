from itertools import permutations


N, M, R = map(int, input().split())
r = list(map(int, input().split()))
INF = float('inf')

graph = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

distance = [[float('inf') for _ in range(N)] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

total_min = INF
for i in permutations(r, len(r)):
    total = 0
    for j in range(len(r)-1):
        total += graph[i[j]-1][i[j-1]-1]
    if total < total_min:
        total_min = total

print(total_min)

