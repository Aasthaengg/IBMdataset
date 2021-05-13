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

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
P = [int(sys.stdin.readline()) for _ in range(N)]

# dp[i]: i より前に何個連続してるか
dp = np.zeros(N + 1, dtype=int)
for i in range(N):
    p = P[i]
    dp[p] = dp[p - 1] + 1
print(N - dp.max())
