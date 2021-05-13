from heapq import heappop, heappush

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]
for a, b, c in X:
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))


def dijkstra(s):
    inf = 10 ** 9 + 7
    d = [inf] * N
    d[s] = 0
    pq = []
    heappush(pq, (0, s))
    while pq:
        _, u = heappop(pq)
        for v, c in graph[u]:
            if d[v] > d[u] + c:
                d[v] = d[u] + c
                heappush(pq, (d[v], v))

    return d


dist = [dijkstra(s) for s in range(N)]
ans = [False] * M
for n, (a, b, c) in enumerate(X):
    for i in range(N):
        for j in range(N):
            ans[n] |= dist[i][j] == dist[i][a - 1] + c + dist[j][b - 1]

print(M - sum(ans))
