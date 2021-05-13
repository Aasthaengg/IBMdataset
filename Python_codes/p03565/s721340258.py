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
T = list(s())
l1 = len(S)
l2 = len(T)
Flag =  0
for i in range(l1-l2+2):
    if S[i:i+l2] == T:
        Flag = 1
        break
if Flag == 1:
    for i in range(l1):
        if S[i] == '?':
            S[i] = 'a'
    print(''.join(S))
    exit()
for i in range(l1-l2,-1,-1):
    s = S[i:i+l2]
    Flag = 1
    for j in range(l2):
        if s[j] != T[j] and s[j] != '?':
            Flag = 0
            break
    if Flag:
        for j in range(i,i+l2):
            if S[j] == '?':
                S[j] = T[j-i]
        for i in range(l1):
            if S[i] == '?':
                S[i] = 'a'
        print(''.join(S))
        exit()
print('UNRESTORABLE')