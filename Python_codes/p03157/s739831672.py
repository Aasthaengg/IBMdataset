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
S = [input() for _ in range(H)]

ans = 0
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
check = [[0]*W for _ in range(H)]

for y0 in range(H):
	for x0 in range(W):
		if S[y0][x0] ==  "." or check[y0][x0] == 1:
			continue
		cnt_black = 1
		cnt_white = 0
		check[y0][x0] = 1
		q = deque([(y0, x0)])
		while q:
			#print(q)
			y, x = q.popleft()
			for i in range(4):
				ny = y + dy[i]
				nx = x + dx[i]
				if 0 <= ny < H and 0 <= nx < W:
					if S[y][x] == "#" and S[ny][nx] == "." and check[ny][nx] == 0:
						check[ny][nx] = 1
						#print((y0, x0), (ny, nx))
						cnt_white += 1
						q.append((ny, nx))
					if S[y][x] == "." and S[ny][nx] == "#" and check[ny][nx] == 0:
						check[ny][nx] = 1
						cnt_black += 1
						q.append((ny, nx))
		ans += cnt_white*cnt_black
print(ans)
