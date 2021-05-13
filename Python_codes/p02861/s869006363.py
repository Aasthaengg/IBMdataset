import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline.rstrip()
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
def inplt(n): return [tuple(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n = inp()
XY = [(0,0)] + inplt(n)

P = permutations(range(1,n+1))
ans = 0
s = 0
for l in P:
    for i in range(1,n):
        s += math.sqrt((XY[l[i]][0]-XY[l[i-1]][0])**2 + (XY[l[i]][1]-XY[l[i-1]][1])**2)
        
ans = s/math.factorial(n)
print(ans)