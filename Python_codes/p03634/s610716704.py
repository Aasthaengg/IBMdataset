import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
    Q, K = map(int, input().split())
    K -= 1
    X = []
    Y = []
    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        X.append(x)
        Y.append(y)

    que = queue.Queue()
    INF = 10 ** (25)
    dist = [INF for _ in range(N)]
    dist[K] = 0
    que.put(K)
    while not que.empty():
        cn = que.get()
        for nn, c in G[cn]:
            if dist[nn] > dist[cn] + c:
                dist[nn] = dist[cn] + c
                que.put(nn)

    for x, y in zip(X, Y):
        print(dist[x] + dist[y])


if __name__ == '__main__':
    main()
