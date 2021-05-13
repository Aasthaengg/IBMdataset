import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n,m = inpm()
s = [[0] * n for i in range(m)]
for i in range(m):
    tmp = inpl()
    for j in range(len(tmp) - 1):
        s[i][tmp[j+1]-1] = 1
p = inpl()

ans = 0
for i in range(2**n):
    for j in range(m):
        cnt = 0
        for k in range(n):
            if s[j][k] == 1 and (i >> k) & 1 == 1:
                cnt += 1
        if p[j] != (cnt % 2):
            break
    else:
        ans += 1
        continue
print(ans)