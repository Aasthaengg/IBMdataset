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
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

A, B, Q = MAP()
s = [INT() for _ in range(A)]
t = [INT() for _ in range(B)]

for _ in range(Q):
	x = INT()
	idx_s = bisect(s, x)
	idx_t = bisect(t, x)

	S = []
	T = []
	if 0 < idx_s:
		S.append(s[idx_s-1])
	if idx_s < A:
		S.append(s[idx_s])

	if 0 < idx_t:
		T.append(t[idx_t-1])
	if idx_t < B:
		T.append(t[idx_t])

	ans = INF
	for shrine, temple in product(S, T):
		if min(shrine, temple) <= x <= max(shrine, temple):
			tmp = abs(shrine-temple) + min(abs(x-shrine), abs(x-temple))
		else:
			tmp = max(abs(x-shrine), abs(x-temple))
		ans = min(ans, tmp)

	print(ans)

