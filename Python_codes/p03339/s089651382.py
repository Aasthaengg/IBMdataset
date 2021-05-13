import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N = i()
S = list(s())
w = [0]*N
e = [0]*N
for i in range(N):
    if S[i] == 'W':
        w[i] = 1
    if S[i] == 'E':
        e[i] = 1
w = [0]+list(itertools.accumulate(w))
e = [0]+list(itertools.accumulate(e[::-1]))
e.reverse()
ans = 10**9
for i in range(N+1):
    ans = min(ans,w[i]+e[i])
print(ans)
