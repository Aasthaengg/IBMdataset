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
#import numpy as np
#decimal.getcontext().prec = 10

A, B, C, D, E, F = MAP()

ans = (-1, 0, 0)
for w1 in range(0, F+1, 100*A):
	for w2 in range(0, F-w1+1, 100*B):
		w = w1+w2
		for s1 in range(0, min(F-w+1, w*E//100+1), C):
			for s2 in range(0, min(F-w-s1+1, w*E//100-s1+1), D):
				s = s1+s2
				a = w+s
				ans = max(ans, (s/a if a != 0 else -1, a, s))

print(ans[1], ans[2])
