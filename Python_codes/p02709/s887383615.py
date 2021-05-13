import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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

N = INT()
A = LIST()

L = [[x, i] for i, x in enumerate(A)]
L.sort()
dp = [[-1]*N for _ in range(N)]

def rec(l, r):
	if l > r:
		return 0
	if dp[l][r] >= 0:
		return dp[l][r]
	idx = r-l  # 次に選ぶ幼児
	val, i = L[idx]
	dp[l][r] = max(abs(i-l)*val + rec(l+1, r), abs(r-i)*val + rec(l, r-1))
	return dp[l][r]

print(rec(0, N-1))
