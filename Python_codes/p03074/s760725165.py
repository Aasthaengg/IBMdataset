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

N, K = MAP()
S = [int(s) for s in input()] + [1]

r = -1
ans = 0
cnt = 0
used = [0]*(N + 1)
for l in range(N):
    if S[l] + S[l-1] == 0:
        continue
    while r < N and used[r] - used[l-1] <= K:
        r += 1
        if S[r-1] == 1 and S[r] == 0:
            used[r] = used[r - 1] + 1
        else:
            used[r] = used[r - 1]
    ans = max(ans, r-l)

print(ans)
