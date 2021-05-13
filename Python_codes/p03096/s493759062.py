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
    n = ni()
    last = [-1 for _ in range(2 * 10 ** 5 + 1)]
    d = []
    dp = [INF for _ in range(n + 1)]
    dp[0] = 1

    prev = -1
    for i in range(n):
        di = ni()
        di -= 1
        if i > 0:
            if prev == di:
                d.append(-1)
                prev = di
                continue
        d.append(di)
        prev = di

    for i, di in enumerate(d):
        dp[i + 1] = dp[i]
        if di == -1:
            last[di] = i
            continue
        if last[di] != -1:
            if i - last[di] != -1:
                dp[i + 1] += dp[last[di] + 1]
                dp[i + 1] %= MOD
        last[di] = i

    print(dp[n])


if __name__ == '__main__':
    main()
