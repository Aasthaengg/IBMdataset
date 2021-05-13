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

# import heapq
# from collections import deque
# import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n, a, b = ns()

    if n == 2:
        print(1)
        exit(0)

    if a > b:
        print(0)
        exit(0)

    if n==1:
        if a==b:
            print(1)
            exit(0)
        else:
            print(0)
            exit(0)

    minimum_sum = a * n + (b - a)
    maximum_sum = b * n - (b - a)
    print(maximum_sum - minimum_sum + 1)


if __name__ == '__main__':
    main()
