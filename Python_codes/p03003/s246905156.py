import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
S = LIST()
T = LIST()

dp = []
for i in range(N+1):
	dp.append([0]*(M+1))
# print(dp)

for i in range(1, N+1):
	for j in range(1, M+1):
		if S[i-1] == T[j-1]:
			dp[i][j] = (1 + dp[i-1][j] + dp[i][j-1]) % mod
		else:
			dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % mod
ans = (dp[-1][-1] + 1) % mod
print(ans)
