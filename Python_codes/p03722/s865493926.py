N, M = map(int, input().split())
egdes = [list(map(int, input().split())) for _ in range(M)]

INF = 10 ** 13
dist = [INF] * (N + 1)
dist[1] = 0
for _ in range(N - 1):
    for a, b, c in egdes:
        dist[b] = min(dist[b], dist[a] - c)
ans = dist[N]
for a, b, c in egdes:
    dist[b] = min(dist[b], dist[a] - c)
print(-ans if ans == dist[N] else 'inf')
