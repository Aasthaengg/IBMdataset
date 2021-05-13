import sys
import math
import collections
import bisect
import copy

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    h, w = ns()
    mat = [list(input()) for _ in range(h)]
    visited = [[False for _ in range(w)] for __ in range(h)]

    B, W = 0, 1
    for y in range(h):
        for x in range(w):
            if mat[y][x] == "#":
                mat[y][x] = B
            else:
                mat[y][x] = W

    cnt = [0, 0]
    pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(y, x, here):
        visited[y][x] = True
        cnt[here] += 1

        for yi, xi in pos:
            ty = y + yi
            tx = x + xi
            if 0 <= ty < h and 0 <= tx < w:
                if not visited[ty][tx] and mat[ty][tx] == here ^ 1:
                    bfs(ty, tx, here ^ 1)

    ans = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x]:
                cnt = [0, 0]
                bfs(y, x, mat[y][x])
                ans += cnt[B] * cnt[W]

    print(ans)


if __name__ == '__main__':
    main()
