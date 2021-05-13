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
A, B = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))

P = np.array(P, dtype=int)
c1 = (P <= A).sum()
c2 = (B < P).sum()
c3 = N - c1 - c2

print(min(c1, c2, c3))
