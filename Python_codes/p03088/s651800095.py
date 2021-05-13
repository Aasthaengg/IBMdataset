import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

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
    n = ni()
    a, c, g, t = 0, 1, 2, 3
    dic = {0: "A", 1: "C", 2: "G", 3: "T"}

    dp = [[[[0 for _ in range(4)] for __ in range(4)] for ___ in range(4)] for ____ in range(n + 1)]
    dp[0][t][t][t] = 1

    for x in range(n):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if [j, k, l] not in [[a, g, c], [g, a, c], [a, c, g]]:
                            if [i, j, l] != [a, g, c]:
                                if [i, k, l] != [a, g, c]:
                                    dp[x + 1][j][k][l] += dp[x][i][j][k]
                                    dp[x + 1][j][k][l] %= MOD

    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[n][i][j][k]
                ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
