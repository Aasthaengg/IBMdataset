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

H, W = MAP()
s = ["#"*(W+2)] + ["#"+input()+"#" for _ in range(H)] + ["#"*(W+2)]

white = 0
for i in range(1, H+1):
	for j in range(1, W+1):
		if s[i][j] == ".":
			white += 1

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

q = deque()
q.append((1, 1))
dist = [[-1]*(W+2) for _ in range(H+2)]
dist[1][1] = 0
cnt = 0
while q:
	y, x = q.popleft()
	for i in range(4):
		ny = y+dy[i]
		nx = x+dx[i]
		if s[ny][nx] == "." and dist[ny][nx]==-1:
			dist[ny][nx] = dist[y][x]+1
			q.append((ny, nx))

print(white-dist[H][W]-1 if dist[H][W] != -1 else -1)
