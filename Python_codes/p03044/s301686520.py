import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N = int(readline())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, readline().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    color = [0] * N

    def dfs(v, p, c):
        color[v] = c
        for nv, w in G[v]:
            if nv == p:
                continue
            if w % 2:
                dfs(nv, v, 1 - c)
            else:
                dfs(nv, v, c)

    dfs(0, -1, 0)
    print(*color, sep='\n')
    return


if __name__ == '__main__':
    main()
