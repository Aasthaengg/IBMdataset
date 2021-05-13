import sys
import math
import numpy as np
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

sx,sy,tx,ty = I()
a = ty-sy
b = tx-sx
ans1 = 'U'*a+'R'*b+'D'*a+'L'*(b+1)
ans2 = 'U'*(a+1)+'R'*(b+1)+'D'+'R'+'D'*(a+1)+'L'*(b+1)+'U'
print(ans1+ans2)