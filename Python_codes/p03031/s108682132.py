import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
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

n,m = inpm()
S = inpll(m)
P = inpl()

ans = 0
for bi in itertools.product([0,1],repeat=n):
    for i in range(m):
        cnt = 0
        for j in range(S[i][0]):
            if bi[S[i][j+1]-1] == 1:
               cnt += 1
        if cnt%2 != P[i]:
            break
        else:
            continue
        break
    else:
        ans += 1

print(ans)