INF = 10 ** 15


def bellman_ford(v, G):
    ret = [INF] * len(G)
    ret[v] = 0

    for _ in range(len(G) - 1):
        for u, g in enumerate(G):
            for w, l in g:
                if not ret[u] == INF and ret[w] > ret[u] + l:
                    ret[w] = ret[u] + l

    for _ in range(len(G)):
        for u, g in enumerate(G):
            for w, l in g:
                if not ret[u] == INF and ret[w] > ret[u] + l:
                    ret[w] = -INF

    return ret


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, -c))

ans = bellman_ford(0, G)[-1]
print('inf' if ans == -INF else -ans)
