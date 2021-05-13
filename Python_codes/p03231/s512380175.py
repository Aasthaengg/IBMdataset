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
 
N,M = I()
S = list(s())
T = list(s())
n = lcm(N,M)
l = (N-1)//(n//M)
for i in range(l+1):
    if S[i*(n//M)] != T[i*(n//N)]:
        print(-1)
        exit()
print(n)