import sys

N, M = map(int, input().split())

graph = [0] * (M)
for m in range(M):
    a, b, c = map(int, input().split())
    graph[m] = (a, b, -c)

INF = 1e18
distance = [INF] * N
distance[0] = 0

for n in range(N):
    for i in range(M):
        a, b, c = graph[i]
        if INF != distance[a - 1] and distance[b - 1] > distance[a - 1] + c:
            distance[b - 1] = distance[a - 1] + c
            if b == N and n == N - 1:
                print("inf")
                sys.exit()

print(-distance[N - 1])