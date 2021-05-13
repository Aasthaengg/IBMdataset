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


AB = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

graph = [[] for _ in range(5)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)

ok = False
for a, b, c, d in itertools.permutations(range(1, 5)):
    ok |= b in graph[a] and c in graph[b] and d in graph[c]
if ok:
    print('YES')
else:
    print('NO')
