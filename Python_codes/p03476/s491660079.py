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

lim = 10**5

is_prime = [1]*(lim+1)
is_prime[0] = 0
is_prime[1] = 0

for i in range(lim+1):
	if is_prime[i] == 1:
		for j in range(2, lim//i + 1):
			is_prime[i*j] = 0

dp = [0]*(lim+1)
for i in range(lim+1):
	if is_prime[i] and is_prime[(i+1)//2]:
		dp[i] = 1

dp = list(accumulate(dp))

Q = INT()
for _ in range(Q):
	l, r = MAP()
	print(dp[r]-dp[l-1])

