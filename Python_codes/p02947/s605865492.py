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

n = k()
dict_a = {}

for i in range(n):
    s = "".join(sorted(input()))
    if s in dict_a:
        dict_a[s] += 1
        cnt += dict_a[s]
    else:
        dict_a[s] = 0

print(cnt)
