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

n, m = MAP()
c = LIST()

dp = [INF]*(n+1)
dp[0] = 0

for i in range(n+1):
	for j in c:
		if i-j >= 0:
			dp[i] = min(dp[i], dp[i-j]+1)
# print(dp)
print(dp[n])

