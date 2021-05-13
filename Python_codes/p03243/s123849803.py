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

N = s()
if int(N) <= int(N[0]*len(N)):
    print(N[0]*len(N))
else:
    if N[0] == 9:
        print('1'+0*len(N))
    else:
        print(str(int(N[0])+1)*len(N))
