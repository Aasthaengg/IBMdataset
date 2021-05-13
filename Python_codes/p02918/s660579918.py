import sys

# import re
import math
import collections
# import decimal
# import bisect
# import itertools
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
    n, k = ns()
    s = list(input())

    cnt = 0
    happy = 0
    for i in range(1, n):
        if s[i - 1] != s[i]:
            cnt += 1
        else:
            happy += 1

    kaisu = (cnt + 1) // 2
    tmp = -1 if cnt % 2 else 0

    ans = min(2 * kaisu + tmp, 2 * k)

    print(ans + happy)


if __name__ == '__main__':
    main()
