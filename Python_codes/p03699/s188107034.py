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
S = [i() for _ in range(N)]
S.sort()
ans = sum(S)
num = 0
for i in range(N):
    if S[i]%10 != 0:
        num = S[i]
        break
if ans%10 == 0:
    ans = ans-num
if ans%10 == 0:
    ans = 0
print(ans)