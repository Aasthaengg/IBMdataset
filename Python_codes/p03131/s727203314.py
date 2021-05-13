import sys
import re
import math
import collections
import decimal
import bisect
import itertools

import copy

# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    k, a, b = ns()
    ans = 0
    if b - a < 2:
        ans = k + 1
    else:
        if k - a <= 0:
            ans = k + 1
        else:
            ans = a + (k + 1 - a) // 2 * (b-a) + (k + 1 - a) % 2

    print(ans)


if __name__ == '__main__':
    main()
