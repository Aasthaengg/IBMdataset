import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===
def main():
    n, c, k = ns()
    t = [ni() for _ in range(n)]
    t.sort()

    ans = 0
    idx = 0
    while idx < n:
        ans += 1

        k_idx = bisect.bisect_right(t, t[idx] + k)
        c_idx = idx + c

        idx = min(k_idx, c_idx)

    print(ans)


if __name__ == '__main__':
    main()
