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

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N = int(sys.stdin.buffer.readline())

VACANT = 'Vacant'
FEMALE = 'Female'
MALE = 'Male'


def check(n):
    print(n, flush=True)
    s = sys.stdin.buffer.readline().decode().rstrip()
    if s == VACANT:
        exit()
    return s


l = 0
h = N
ls = check(l)
while abs(l - h) > 1:
    mid = (l + h) // 2
    ms = check(mid)
    if ((mid - l) % 2 == 0) == (ls == ms):
        l = mid
        ls = ms
    else:
        h = mid
check(h)
check(l)
