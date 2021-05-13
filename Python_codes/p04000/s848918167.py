import bisect
import heapq
import itertools
import math
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18

H, W, N = list(map(int, sys.stdin.readline().split()))
AB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

hist = set()

count = defaultdict(int)
for dx, dy in itertools.product([0, 1, 2], repeat=2):
    for a, b in AB:
        count[(a + dx, b + dy)] += 1
ans = [0] * 10
for [a, b], cnt in count.items():
    if 3 <= a <= H and 3 <= b <= W:
        ans[cnt] += 1
print((H - 2) * (W - 2) - sum(ans[1:]))
print('\n'.join(map(str, ans[1:])))
