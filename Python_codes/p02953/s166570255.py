import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
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

N = i()
H = l()
H[0] -= 1
for i in range(N-1):
    if H[i] > H[i+1]:
        print('No')
        exit()
    elif H[i] != H[i+1]:
        H[i+1] -= 1
print('Yes')