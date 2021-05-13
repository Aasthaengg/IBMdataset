import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")

N = k()
A = l()
Cnt = [0] * (N+1)
for a in A:
    Cnt[a] += 1
for c in Cnt:
    ans += c * (c-1) // 2
Ans = [ans - Cnt[a] + 1 for a in A]
print("\n".join(map(str, Ans)))
