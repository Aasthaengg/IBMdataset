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

n,q=I()
s = v()
t = [0]*(n+1)
for i in range(n):
    t[i+1]=t[i]+(1 if s[i:i+2]=="AC" else 0)

ans = []
for i in range(q):
    l,r=I()
    ans.append(t[r-1]-t[l-1])
for i in ans:
    print(i)
