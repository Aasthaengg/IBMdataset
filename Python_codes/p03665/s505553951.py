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
	
N, P = MAP()
A = LIST()

dp = [[0, 0] for _ in range(N+1)]
dp[0][0] = 1
dp[0][1] = 0  #dp[0]は一個も選ばないときのP=0,P=1になる組み合わせ

for i, a in enumerate(A):
	if a%2 == 0:
		dp[i+1][0] = dp[i][0] * 2
		dp[i+1][1] = dp[i][1] * 2
	else:
		dp[i+1][0] = dp[i][1] + dp[i][0]
		dp[i+1][1] = dp[i][0] + dp[i][1]

print(dp[N][P])