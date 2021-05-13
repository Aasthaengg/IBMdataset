import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    r, c, k = ns()

    mat = [[0 for _ in range(c + 1)] for __ in range(r + 1)]
    for _ in range(k):
        x, y, v = ns()
        x, y = x - 1, y - 1
        mat[x][y] = v

    dp = [[0] * 4 for _ in range(c + 1)]

    for i in range(r):
        ndp = [[0] * 4 for _ in range(c + 1)]
        for j in range(c):
            for n in range(2, -1, -1):
                dp[j][n + 1] = max(dp[j][n + 1], dp[j][n] + mat[i][j])

            ndp[j][0] = max(dp[j])
            for n in range(4):
                dp[j + 1][n] = max(dp[j + 1][n], dp[j][n])
        dp = ndp

    print(max(dp[c - 1]))


if __name__ == '__main__':
    main()
