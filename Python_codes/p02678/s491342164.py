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
mod = 10**9+7

N,M = I()
A = [I() for _ in range(M)]
links = [[] for _ in range(N)]
ans = [-1]*(N)
ans[0] = 0
for a,b in A:
    links[a-1].append(b-1)
    links[b-1].append(a-1)
que = deque([0])
while que:
    i = que.pop()
    for j in links[i]:
        if ans[j] == -1:
            ans[j] = i+1
            que.appendleft(j)
print('Yes')
for i in range(1,N):
    print(ans[i])