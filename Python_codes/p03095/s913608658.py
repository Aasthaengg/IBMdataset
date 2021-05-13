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
    s = input()

    c = collections.Counter(s)

    ans = 1
    for v in c.values():
        ans *= v + 1
        ans %= MOD
    ans = (ans - 1) % MOD
    print(ans)


if __name__ == '__main__':
    main()
