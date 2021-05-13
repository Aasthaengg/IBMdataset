import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    edge = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edge[u].append((v, w))
        edge[v].append((u, w))

    color = [False] * N
    color[0] = 0
    q = deque([1])

    while q:
        u = q.popleft()
        c1 = color[u - 1]
        for c, w in edge[u]:
            if color[c - 1] is False:
                q.append(c)
                color[c - 1] = (c1 + w) % 2

    print(*color)


if __name__ == "__main__":
    main()
