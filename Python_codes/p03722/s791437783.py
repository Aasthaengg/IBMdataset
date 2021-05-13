import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict
    n, m = map(int, readline().split())
    edge = []

    for _ in range(m):
        a, b, c = map(int, readline().split())
        edge.append((a - 1, b - 1, -c))

    dist = [INF] * n
    dist[0] = 0

    for i in range(n - 1):
        for a, b, c in edge:
            dist[b] = min(dist[b], dist[a] + c)

    loop = [False] * n
    for i in range(n):
        for a, b, c in edge:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                loop[b] = True

    if loop[n - 1]:
        print("inf")
    else:
        print(-dist[n - 1])


if __name__ == '__main__':
    main()
