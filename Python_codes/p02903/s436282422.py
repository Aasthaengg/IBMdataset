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

H, W, A, B = list(map(int, sys.stdin.buffer.readline().split()))

ans = np.zeros((H, W), dtype='U1')
ans[:B, :A] = '1'
ans[:B, A:] = '0'
ans[B:, A:] = '1'
ans[B:, :A] = '0'
print('\n'.join(map(lambda r: ''.join(r), ans)))
