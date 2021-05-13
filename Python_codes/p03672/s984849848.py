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

S = s()
N = len(S)
ans = 0
for i in range(1,N-1,2):
    a = S[:i+1]
    if a[:(i+1)//2] == a[(i+1)//2:]:
        ans = i+1
print(ans)