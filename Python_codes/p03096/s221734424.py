import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
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
C = [INT() for _ in range(N)]

dp = [0]*(N+1)
dp[0] = 1
dp2 = [-1]*(max(C)+1) #前に色iが出てきたインデックスの保存

for i in range(1, N+1):
	p = dp2[C[i-1]]
	if 1 < i-p and p != -1:
		dp[i] += dp[p]
	dp[i] += dp[i-1]
	dp2[C[i-1]] = i
	dp[i] %= mod

print(dp[N])
