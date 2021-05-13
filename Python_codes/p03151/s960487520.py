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
    n = ni()
    a = na()
    b = na()

    if sum(a) < sum(b):
        print(-1)
        exit(0)

    d = []
    for ai, bi in zip(a, b):
        d.append(ai - bi)

    d.sort()
    poor = 0
    ans_cnt = 0
    for di in d:
        if di < 0:
            ans_cnt += 1
            poor += di

    d.sort(reverse=True)
    for di in d:
        if poor < 0:
            poor += di
            ans_cnt += 1
        else:
            break

    print(ans_cnt)


if __name__ == '__main__':
    main()
