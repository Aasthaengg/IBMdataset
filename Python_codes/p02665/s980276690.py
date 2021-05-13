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
sys.setrecursionlimit(10**7)
MOD = 10**9 + 7; EPS = sys.float_info.epsilon
PI = np.pi; EXP = np.e; INF = np.inf

n = iinput()
a = iarr()

cum = []; sum = 0
for num in a: sum += num; cum.append(sum)

ans = 1
now = 1
for i in range(n+1):
    next = min(2*(now - a[i]), cum[n]-cum[i])
    now = next
    if n==i and next<0 : ans = -1; break
    if n!=i and next<=0 : ans = -1; break
    ans += next

#if a[n] > 2**n: ans = -1
print(ans)

