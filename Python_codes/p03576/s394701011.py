import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan, degrees
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K = MAP()
xy = [LIST() for _ in range(N)]
X = sorted([x[0] for x in xy])
Y = sorted([x[1] for x in xy])

ans = INF
for p in combinations(X, 2):
	x_min = p[0]
	x_max = p[1]
	for q in combinations(Y, 2):
		y_min = q[0]
		y_max = q[1]
		
		cnt = 0
		for x, y in xy:
			if x_min <= x <= x_max and y_min <= y <= y_max:
				cnt += 1
		if cnt >= K:
			ans = min(ans, (x_max-x_min)*(y_max-y_min))
print(ans)
