import numpy as np
import scipy.sparse as sps
import scipy.misc as spm
import collections as col
import functools as func
import itertools as ite
import fractions as frac
import math as ma
from math import cos,sin,tan,sqrt
import cmath as cma
import copy as cp
import sys
import re
sys.setrecursionlimit(10**7)
EPS = sys.float_info.epsilon
PI = np.pi; EXP = np.e; INF = np.inf
MOD = 10**9 + 7

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
def adj(n): return [[] for _ in range(n)]

n,q = imap()
g = adj(n+1)
for i in range(n-1):
    a,b = imap()
    g[a].append(b)
    g[b].append(a)

cnt = iarr(n+1)
for i in range(q):
    p,x = imap()
    cnt[p] += x

que = col.deque([1])
dep = col.defaultdict(int)
dep[1] = 1
while que:
    now = que.popleft()
    for next in g[now]:
        if dep[next]: continue
        # dep更新、que更新、そのほか　＝３点セット
        dep[next] = dep[now] + 1
        que.append(next)
        cnt[next] += cnt[now]

print(*cnt[1:])
    
