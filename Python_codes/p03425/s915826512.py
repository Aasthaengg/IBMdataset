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

    inis = [s[0] for s in S if s[0] == 'M' or s[0] == 'A' or s[0] == 'R' or s[0] == 'C' or s[0] == 'H']
    c = Counter(inis)
    ans = 0
    for tpl in list(combinations(c.values(), 3)):
        ans += list(accumulate(tpl, mul))[-1]

    print(ans)


if __name__ == '__main__':
    main()
