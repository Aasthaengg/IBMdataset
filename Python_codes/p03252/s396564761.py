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
mod = 10**9+7

S = list(s())
T = list(s())
N = len(S)
s = [[] for _ in range(26)]
t = [[] for _ in range(26)]
for i in range(N):
    s[ord(S[i])-97].append(i)
    t[ord(T[i])-97].append(i)
for i in range(26):
    s[i].sort()
    t[i].sort()
for i in range(26):
    if s[i] not in t:
        print('No')
        exit()
print('Yes')