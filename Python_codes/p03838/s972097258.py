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
    x, y = ns()

    ans = abs(abs(x) - abs(y))

    if 0 < y < x:
        ans += 2
    elif 0 > x > y:
        ans += 2
    elif x > 0 and y < 0:
        ans += 1
    elif x < 0 and y > 0:
        ans += 1
    elif x > 0 and y == 0:
        ans += 1
    elif x == 0 and y < 0:
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
