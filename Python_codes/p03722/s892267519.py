def bellman_ford(es: list, s: int, inf: int) -> list:
    n = 0
    for e in es: n = max(n, e[0], e[1])
    n += 1
    dis = [inf] * n
    dis[s] = 0
    for t in range(n << 1):
        for e in es:
            if dis[e[0]] != inf and dis[e[1]] > dis[e[0]] + e[2]:
                dis[e[1]] = dis[e[0]] + e[2]
                if t + 1 >= n: dis[e[1]] = -inf
    return dis

if __name__ == '__main__':
    N, M = map(int, input().split())
    es = []
    for i in range(M):
        a, b, c = map(int, input().split())
        es.append((a - 1, b - 1, -c))
    INF = 1 << 60
    dis = bellman_ford(es, 0, INF)
    if dis[N - 1] == -INF: print("inf")
    else: print(-dis[N - 1])