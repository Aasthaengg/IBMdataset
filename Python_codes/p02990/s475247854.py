import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
MOD = 10 ** 9 + 7
N,K = map(int,input().split())
fac = [1, 1]
inv = [0, 1]
finv = [1, 1]
for i in range(2, N+1):
    fac.append(fac[-1] * i % MOD)
    inv.append(MOD - inv[MOD%i] * (MOD//i) % MOD)
    finv.append(finv[-1] * inv[-1] % MOD) 
def comb_mod(n, r, m):
    if (n<0 or r<0 or n<r): return 0
    r = min(r, n-r)
    return fac[n] * finv[n-r] * finv[r] % m
ans = 0
for i in range(1,K+1):
    c = comb_mod(K-1,i-1,MOD)
    d = comb_mod(N-K+1,i,MOD)
    ans = c * d
    print(ans%MOD)