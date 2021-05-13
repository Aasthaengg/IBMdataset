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
s = [-INF] + [INT() for _ in range(A)] + [INF]
t = [-INF] + [INT() for _ in range(B)] + [INF]

for _ in range(Q):
	x = INT()
	idx_s = bisect(s, x)
	idx_t = bisect(t, x)

	ans = INF
	for S, T in product([idx_s, idx_s-1], [idx_t, idx_t-1]):
		if min(s[S], t[T]) <= x <= max(s[S], t[T]):
			tmp = abs(s[S]-t[T]) + min(abs(x-s[S]), abs(x-t[T]))
		else:
			tmp = max(abs(x-s[S]), abs(x-t[T]))
		ans = min(ans, tmp)

	for S in [idx_s, idx_s-1]:
		for T in [idx_t, idx_t-1]:
			tmp = min(abs(x-s[S])+abs(s[S]-t[T]), abs(x-t[T])+abs(s[S]-t[T]))
			ans = min(ans, tmp)

	print(ans)

