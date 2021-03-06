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


N = int(sys.stdin.buffer.readline())
ans = 0
for d in range(1, math.ceil(math.sqrt(N)) + 10):
    if (N - d) % d == 0:
        m = (N - d) // d
        if m > 0 and N // m == N % m:
            ans += m

print(ans)
