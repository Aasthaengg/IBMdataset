import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n,m = inpm()
SC = inpll(m)

ans = -1
for i in range(1000):
    if len(str(i)) != n:
        continue
    
    flg = True
    for sc in SC:
        if len(str(i)) < sc[0]:
            flg = False
            break
        if str(i)[sc[0]-1] != str(sc[1]):
            flg = False
            break
    if flg == True:
        ans = i
        break

print(ans)