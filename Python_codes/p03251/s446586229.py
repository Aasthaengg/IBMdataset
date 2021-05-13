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

N,M,X,Y = I()
x = l()
y = l()
x1 = max(x)
y1 = min(y)
for z in range(X+1,Y+1):
    if x1 < z and y1 >= z:
        print('No War')
        exit()
print('War')