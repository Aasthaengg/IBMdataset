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
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7

N,C,K = I()
T = [i() for _ in range(N)]
T.sort()
T = deque(T)
ans = [[] for _ in range(N)]
ans[0].append(T.popleft())
now = 0
while T:
    a = T.popleft()
    if len(ans[now]) == C or a-ans[now][0] > K:
        now += 1
    ans[now].append(a)
print(now+1)