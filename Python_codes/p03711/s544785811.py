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
INF = 10**9
mod = 10**9+7

a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
x,y = I()
if (x in a and y in a) or (x in b and y in b) or x == y == 2:
    print('Yes')
else:
    print('No')