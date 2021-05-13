import sys
import re
import math
import collections
import decimal
import bisect
import itertools

# import copy
# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize
# MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, k, s = ns()
    res = [0 for i in range(n)]

    for i in range(n):
        if i < k:
            res[i] = s
        else:
            if s == 10**9:
                res[i] = 10**9-1
            else:
                res[i] = 10**9

    print(*res, sep=" ")


if __name__ == '__main__':
    main()
