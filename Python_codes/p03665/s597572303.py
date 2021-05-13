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
lim = 50  #必要そうな階乗の限界を入力
fact = [1] * (lim+1)
for n in range(1, lim+1):
	fact[n] = n * fact[n-1] % mod

#階乗の逆元#
fact_inv = [1]*(lim+1)
fact_inv[lim] = pow(fact[lim], mod-2, mod)
for n in range(lim, 0, -1):
	fact_inv[n-1] = n*fact_inv[n]%mod

def C(n, r):
	return (fact[n]*fact_inv[r]%mod)*fact_inv[n-r]%mod


	
N, P = MAP()
A = LIST()

a = [x%2 for x in A]
cnt_0 = a.count(0)
cnt_1 = a.count(1)

ans = 2**cnt_0

if P == 0:
	c = 0
	for i in range(cnt_1//2 + 1):
		c += C(cnt_1, 2*i)
	print(ans*c)
elif P == 1:
	c = 0
	for i in range((cnt_1-1)//2 + 1):
		c += C(cnt_1, 2*i+1)
	print(ans*c)

