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
#import numpy as np
from decimal import *

H, W = MAP()
A = [input() for _ in range(H)]
cnt = [[-1]*W for _ in range(H)]
q = deque()

for y in range(H):
    for x in range(W):
        if A[y][x] == "#":
            cnt[y][x] = 0
            q.append((y, x))

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W and cnt[ny][nx] == -1:
            cnt[ny][nx] = cnt[y][x] + 1
            q.append((ny, nx))

ans = 0
for i in range(H):
    ans = max(ans, max(cnt[i]))
print(ans)
