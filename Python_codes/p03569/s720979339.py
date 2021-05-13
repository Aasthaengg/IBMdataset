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

S = sys.stdin.buffer.readline().decode().rstrip()

t = S.replace('x', '')
if t != t[::-1]:
    print(-1)
    exit()

l = 0
r = len(S) - 1
ans = 0
while l < r:
    while S[l] != S[r]:
        if S[l] != 'x':
            r -= 1
        else:
            l += 1
        ans += 1
    l += 1
    r -= 1

print(ans)
