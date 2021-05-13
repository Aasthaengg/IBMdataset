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


N = int(sys.stdin.readline())
A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
C = list(sys.stdin.readline().rstrip())

A = np.array(A, dtype='U1')
B = np.array(B, dtype='U1')
C = np.array(C, dtype='U1')


def count(a, b, c):
    if a == b == c:
        return 0
    if a == b or b == c or c == a:
        return 1
    return 2


ans = 0
for a, b, c in zip(A, B, C):
    ans += count(a, b, c)
print(ans)
