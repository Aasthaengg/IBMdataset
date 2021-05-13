import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    n, c = ns()

    dist = []
    value = []
    dist_r = []
    value_r = []
    for _ in range(n):
        di, vi = ns()
        dist.append(di)
        value.append(vi)
        dist_r.append(c - di)
        value_r.append(vi)

    dist_r.reverse()
    value_r.reverse()

    cum = []
    cum_r = []

    value_sum = 0
    value_max = -INF
    for di, vi in zip(dist, value):
        value_sum += vi
        value_max = max(value_max, value_sum - di)
        cum.append(value_max)

    value_sum = 0
    value_max = -INF
    for di, vi in zip(dist_r, value_r):
        value_sum += vi
        value_max = max(value_max, value_sum - di)
        cum_r.append(value_max)

    ans = 0
    for i in range(n):
        a = cum[i]
        c = cum_r[i]
        b, d = 0, 0
        if i != n - 1:
            b = cum[i] - dist[i] + cum_r[n - 2 - i]
            d = cum_r[i] - dist_r[i] + cum[n - 2 - i]
        ans = max(ans, a, b, c, d)

    print(ans)


if __name__ == '__main__':
    main()
