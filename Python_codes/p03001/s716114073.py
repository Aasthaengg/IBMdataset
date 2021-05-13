import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def s(): return input()
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

w,h,x,y = I()
s = w*h/2
if w % 2 != 0 or h % 2 != 0:
    cnt = 0
else:
    if x == w//2 and y == h // 2:
        cnt =1
    else:
        cnt = 0

print("{} {}".format(s,cnt))
