import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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
mod = 10 ** 9 + 7

H, W = MAP()
S = [input() for _ in range(H)]

ans = 0
searched = [[0]*W for _ in range(H)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(H):
	for j in range(W):
		if searched[i][j] or S[i][j] == ".":
			continue
		num_b = 0
		num_w = 0
		q = deque()
		q.append((i, j))
		num_b += 1
		searched[i][j] = 1
		while q:
			y, x = q.popleft()
			for k in range(4):
				ny = y + dy[k]
				nx = x + dx[k]
				if 0 <= ny <= H-1 and 0 <= nx <= W-1 and not searched[ny][nx] and S[ny][nx] != S[y][x]:
					searched[ny][nx] = 1
					if S[ny][nx] == "#":
						num_b += 1
					else:
						num_w += 1
					q.append((ny, nx))
		ans += num_b*num_w

print(ans)