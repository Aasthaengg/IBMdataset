import bisect
import os
from collections import Counter, deque
from fractions import gcd
from functools import lru_cache
from functools import reduce
import functools
import heapq
import itertools
import math
import numpy as np
import re
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N, H, W = list(map(int, sys.stdin.readline().split()))
A, B = list(zip(*[map(int, sys.stdin.readline().split()) for _ in range(N)]))

A = np.array(A)
B = np.array(B)

print(((A >= H) & (B >= W)).sum())
