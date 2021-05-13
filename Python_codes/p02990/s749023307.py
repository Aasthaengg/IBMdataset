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

#階乗#
lim = 2*10**5   #必要そうな階乗の限界を入力
fact = [1] * (lim+1)
for n in range(1, lim+1):
	fact[n] = n * fact[n-1] % mod

#階乗の逆元#
fact_inv = [1]*(lim+1)
fact_inv[lim] = pow(fact[lim], mod-2, mod)
for n in range(lim, 0, -1):
	fact_inv[n-1] = n*fact_inv[n]%mod

def C(n, r):
	if n < r or n < 0 or r < 0:
		return 0
	else:
		return (fact[n]*fact_inv[r]%mod)*fact_inv[n-r]%mod

N, K = MAP()

if N == K:
	for i in range(1, N+1):
		print(i if i == 1 else 0)
	exit()

for i in range(1, K+1):
	blue = C(K-1, i-1) #青いボールをi個の塊に分ける
	red = (C(N-K-1, i-2) + 2*C(N-K-1, i-1) + C(N-K-1, i))%mod #赤いボールをi-1、i、i+1個の塊に分ける(i個の場合は2パターン)
	print((blue*red)%mod)
