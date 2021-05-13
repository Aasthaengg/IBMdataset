import sys
import math
import collections
import bisect
import copy

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, m = ns()
    a = na()
    cum = [0] * (n + 1)
    cnt = dict()

    for i, ai in enumerate(a):
        tmp = (cum[i] + ai) % m
        cum[i + 1] = tmp
        if tmp not in cnt.keys():
            cnt[tmp] = [i]
        else:
            cnt[tmp].append(i)

    ans = 0
    for l, ci in enumerate(cum):
        if ci in cnt.keys():
            length = len(cnt[ci])
            tmp = bisect.bisect_right(cnt[ci], l - 1)
            ans += length - tmp

    print(ans)


if __name__ == '__main__':
    main()
