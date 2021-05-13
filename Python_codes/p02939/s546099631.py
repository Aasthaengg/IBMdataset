import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
#from decimal import *

S = input()
N = len(S)

dp = [[0, 0] for _ in range(N+1)]
dp[1][0] = 1
 
for i in range(2, N+1):
	if S[i-1] != S[i-2]:
		dp[i][0] = dp[i-1][0] + 1
	else:
		dp[i][0] = dp[i-1][1] + 1

	dp[i][1] = dp[i-2][0] + 1
	#print(dp)

print(dp[-1][0])