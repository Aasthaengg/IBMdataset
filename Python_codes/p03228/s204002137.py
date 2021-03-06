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

A, B, K = list(map(int, sys.stdin.readline().split()))


def op(A, B):
    return A // 2, A // 2 + B


while K:
    if K > 0:
        A, B = op(A, B)
        K -= 1
    if K > 0:
        B, A = op(B, A)
        K -= 1
print(A, B)
