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
    n = ni()
    d = [na() for _ in range(n)]

    d.reverse()

    ans = 0
    for a, b in d:
        if (a + ans) % b > 0:
            ans += b - (a + ans) % b
    print(ans)


if __name__ == '__main__':
    main()
