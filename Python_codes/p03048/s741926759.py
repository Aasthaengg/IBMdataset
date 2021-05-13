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
    r, g, b, n = ns()
    ans = 0
    for i in range(n // r + 1):
        for j in range(n // g + 1):
            tmp = n - r * i - g * j
            if tmp < 0:
                break
            if tmp % b == 0:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
