import numpy as np
import scipy.sparse as sps
import scipy.misc as spm
import collections as col
import functools as func
import itertools as ite
import fractions as frac
import math as ma
import cmath as cma
import copy as cp
import sys
def sinput(): return sys.stdin.readline().strip()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(n=0):
    if n: return [0 for _ in range(n)]
    else: return list(imap())
def farr(): return list(fmap())
def sarr(n=0):
    if n: return ["" for _ in range(n)]
    else: return sinput().split()
def barr(n): return [False for _ in range(n)]
sys.setrecursionlimit(10**7)
MOD = 10**9 + 7; EPS = sys.float_info.epsilon
PI = np.pi; EXP = np.e; INF = np.inf

# 番兵法
h,w = imap()
grid = [[1]*(w+2)] + [[1]+[int(elm == "#") for elm in list(sinput())]+[1] for i in range(h)] + [[1]*(w+2)]

q = col.deque([(1,1)])
dep = col.defaultdict(int)
dep[(1,1)] = 1
while q:
    now = q.popleft()
    if now == (h,w): break
    x,y = now[0],now[1]
    for next in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
        nx,ny = next[0],next[1]
        if grid[nx][ny] or dep[next]: continue # 壁か探索済ならスキップ
        else: dep[next] = dep[now] + 1; q.append(next)

ans = 0
for elm in grid: ans += elm.count(0)
ans = ans - dep[(h,w)] if dep[(h,w)] else -1
print(ans)

