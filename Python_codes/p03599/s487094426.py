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
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

A,B,C,D,E,F = I()
lim1 = F//(100*A)
lim2 = F//(100*B)
ans = 0
ansnum = 0
for i in range(lim1+1):
    for j in range(lim2+1):
        w = 100*i*A+100*j*B
        if i == j == 0:
            continue
        if w > F:
            continue
        r = F-w
        num = 0
        lim3 = min(r,(i*A+j*B)*E)//C
        for k in range(lim3+1):
            num = max(num,k*C+((min(r,(i*A+j*B)*E)-k*C)//D)*D)
        if 100*num/(w+num) > ansnum:
            ans = [w+num,num]
            ansnum = 100*num/(w+num)
if ans == 0:
    print(A*100,0)
else:
    print(*ans)