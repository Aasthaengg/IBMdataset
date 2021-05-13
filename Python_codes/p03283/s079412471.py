import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
import numpy as np
#decimal.getcontext().prec = 10

N, M, Q = MAP()
LR = [LIST() for _ in range(M)]
pq = [LIST() for _ in range(Q)]

x = np.array([[0]*(N+1) for _ in range(N+1)])

for L, R in LR:
	x[L][R] += 1

x = x.cumsum(axis=0).cumsum(axis=1)

for p, q in pq:
	print(x[q][q] - x[q][p-1] - x[p-1][q] + x[p-1][p-1])


