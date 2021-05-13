import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import numpy as np
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N,K = I()
A = l()

def ok(n):
    t = 0
    for a in A:
        if a <= n:
            continue
        t += math.ceil(a/n)-1
    return t <= K

upper = 1000000000
lower = 0
while abs(lower-upper) > 1:
    m = (upper+lower)//2
    if ok(m):
        upper = m
    else:
        lower = m
print(math.ceil(upper))