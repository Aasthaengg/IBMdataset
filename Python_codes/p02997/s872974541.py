import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
nb = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, k = ns()
    ans = []

    tmp = (n - 1) * (n - 2) // 2
    if k > tmp:
        print(-1)
        exit(0)

    for i in range(n - 1):
        ans.append([i, n - 1])

    breakflg = False
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if tmp == k:
                breakflg = True
                break

            tmp -= 1
            ans.append([i, j])

        if breakflg:
            break

    print(len(ans))
    for a, b in ans:
        print(a + 1, b + 1)


if __name__ == '__main__':
    main()
