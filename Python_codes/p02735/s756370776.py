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

H, W = MAP()
s = [input() for _ in range(H)]

cnt = [[-1]*W for _ in range(H)]

if s[0][0] == ".":
	cnt[0][0] = 0
else:
	cnt[0][0] = 1

dy = [0, 1]
dx = [1, 0]

q = deque([(0, 0)])
while q:
	y, x = q.popleft()
	for i in range(2):
		ny = y + dy[i]
		nx = x + dx[i]
		if ny < H and nx < W and cnt[ny][nx] == -1:
			if s[ny][nx] == s[y][x]:
				cnt[ny][nx] = cnt[y][x]
				q.appendleft((ny, nx))
			else:
				cnt[ny][nx] = cnt[y][x] + 1
				q.append((ny, nx))

if s[H-1][W-1] == "#":
	ans = (cnt[H-1][W-1]+1)//2
else:
	ans = (cnt[H-1][W-1])//2
print(ans)
