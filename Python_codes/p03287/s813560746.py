import bisect
import cmath
import heapq
import itertools
import math
import operator
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter, mul, add, xor

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N, M = list(map(int, sys.stdin.buffer.readline().split()))
A = list(map(int, sys.stdin.buffer.readline().split()))

A = np.array([0] + A, dtype=int)
cum = A.cumsum() % M
mods = Counter(cum)


def test():
    N = len(A)
    ans = 0
    for l in range(1, N):
        for r in range(l + 1, N + 1):
            ans += sum(A[l:r]) % M == 0
    print(ans)


# test()
ans = 0
for c in mods.values():
    # c から2選ぶ
    ans += c * (c - 1) // 2
print(ans)
