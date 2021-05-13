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
    n, k = ns()
    a = na()

    total = 0
    for i in range(n):
        for j in range(n):
            if a[i] < a[j]:
                total += 1
                total %= MOD

    ans = total * (k * (k - 1) // 2) % MOD

    cnt = 0
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                cnt += 1
                cnt %= MOD
    cnt = cnt * k % MOD

    res = (ans + cnt) % MOD

    print(res)


if __name__ == '__main__':
    main()
