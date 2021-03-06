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

N, A, B = list(map(int, sys.stdin.readline().split()))
X = list(map(int, sys.stdin.readline().split()))

X = np.array(X)
ans = 0
for d in np.diff(X):
    ans += min(d * A, B)
print(ans)
