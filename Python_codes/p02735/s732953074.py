import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2
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
from decimal import *

H, W = MAP()
s = [input() for _ in range(H)]

dp = [[0]*W for _ in range(H)]

if s[0][0] == ".":
	dp[0][0] = 0
else:
	dp[0][0] = 1


for i in range(1, W):
	if s[0][i] == s[0][i-1]:
		dp[0][i] = dp[0][i-1]
	else:
		dp[0][i] = dp[0][i-1] + 1

for y in range(1, H):
	for x in range(W):
		if x == 0:
			dp[y][x] = dp[y-1][x] + (s[y-1][x] != s[y][x])
		else:
			dp[y][x] = min(dp[y-1][x]+(s[y-1][x] != s[y][x]), dp[y][x-1]+(s[y][x-1] != s[y][x]))

if s[H-1][W-1] == "#":
	dp[H-1][W-1] += 1


print(dp[H-1][W-1]//2)


