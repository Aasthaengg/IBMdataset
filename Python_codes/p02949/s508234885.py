import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict

    n, m, p = map(int, readline().split())
    edge = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, readline().split())
        edge[a - 1].append((b - 1, -c + p))

    dist = [INF] * n
    dist[0] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in edge[u]:
                dist[v] = min(dist[v], dist[u] + w)

    for _ in range(n):
        for u in range(n):
            for v, w in edge[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = -INF

    if dist[n - 1] == -INF:
        print(-1)
    else:
        print(max(-dist[n - 1], 0))


if __name__ == '__main__':
    main()
