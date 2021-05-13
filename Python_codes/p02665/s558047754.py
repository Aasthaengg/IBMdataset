import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    a = na()

    whole = sum(a)

    if n == 0 and a[0] == 0:
        print(-1)
        exit(0)

    ans = 0
    base = 1
    for i in range(n + 1):
        ans += base
        base -= a[i]
        whole -= a[i]
        base = min(base * 2, whole)
        if (base <= 0 and i != n) or (i == n and base != 0):
            print(-1)
            exit(0)

    print(ans)


if __name__ == '__main__':
    main()
