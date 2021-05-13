import bisect
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


H, W = list(map(int, sys.stdin.buffer.readline().split()))
A = [list(sys.stdin.buffer.readline().decode().rstrip()) for _ in range(H)]

S = []
for a in A:
    S += a
counts = Counter(S)


def solve(counts, H, W):
    if H & 1 and W & 1:
        for c in string.ascii_lowercase:
            if counts[c] & 1:
                counts[c] -= 1
                break
        for c in string.ascii_lowercase:
            if counts[c] & 1:
                return False

        cnt = (H + W - 2) // 2
        for c in string.ascii_lowercase:
            if counts[c] % 4:
                counts[c] -= 2
                cnt -= 1
            if cnt < 0:
                return False

    if H & 1 or W & 1:
        if W & 1:
            H, W = W, H
        assert H & 1 == 1

        cnt = W // 2
        for c in string.ascii_lowercase:
            if counts[c] % 4:
                counts[c] -= 2
                cnt -= 1
            if cnt < 0:
                return False

    for c in string.ascii_lowercase:
        if counts[c] % 4:
            return False
    return True


ok = solve(counts, H, W)
if ok:
    print('Yes')
else:
    print('No')

