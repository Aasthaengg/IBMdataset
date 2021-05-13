import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict, deque

    n = int(readline())
    edge = defaultdict(list)

    for i in range(n - 1):
        a, b, c = map(int, readline().split())
        edge[a].append((b, c))
        edge[b].append((a, c))

    q, k = map(int, readline().split())

    que = deque()
    que.append((k, 0))
    dists = dict()

    while que:
        u, dist = que.popleft()
        for v, w in edge[u]:
            if v not in dists:
                dists[v] = dist + w
                que.append((v, dist + w))

    for i in range(q):
        x, y = map(int, readline().split())
        print(dists[x] + dists[y])


if __name__ == '__main__':
    main()
