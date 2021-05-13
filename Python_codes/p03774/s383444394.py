import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
from bisect import bisect_left, insort_left
from heapq import heapify, heappush, heappop

INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
S_MAP = lambda: map(str, INPUT().split())
LIST = lambda: list(map(int, INPUT().split()))
S_LIST = lambda: list(map(str, INPUT().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


def main():
    N, M = MAP()
    AB = [LIST() for _ in range(N)]
    CD = [LIST() for _ in range(M)]

    for a, b in AB:
        dist = INF

        for i, cd in enumerate(CD):
            if dist > abs(a - cd[0]) + abs(b - cd[1]):
                dist = abs(a - cd[0]) + abs(b - cd[1])
                num = i + 1

        print(num)


if __name__ == '__main__':
    main()