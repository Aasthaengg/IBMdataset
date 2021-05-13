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
    N = INT()
    S = [INPUT() for _ in range(N)]

    l = []
    for s in S:
        tmp_l = []
        for c in s:
            tmp_l.append(ord(c))
        tmp_l = sorted(tmp_l)

        tmp_s = ""
        for n in tmp_l:
            tmp_s += chr(n)
        l.append(tmp_s)

    C = Counter(l)
    ans = 0
    for c in C.values():
        if c > 1:
            ans += factorial(c) // (factorial(c - 2) * factorial(2))

    print(ans)


if __name__ == '__main__':
    main()
