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
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

S = list(s())
S.reverse()
for i in range(10**5):
    if not S:
        break

    if ''.join(S[:7][::-1]) == 'dreamer' :
        S = S[7:]
    elif ''.join(S[:6][::-1]) == 'eraser':
        S = S[6:]
    elif ''.join(S[:5][::-1]) == 'dream':
        S = S[5:]
    elif ''.join(S[:5][::-1]) == 'erase':
        S = S[5:]
    else:
        print('NO')
        exit()
print('YES')