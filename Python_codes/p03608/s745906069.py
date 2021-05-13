import numpy as np
import scipy.sparse as sps
import scipy.misc as spm
import collections as col
import functools as func
import itertools as ite
import fractions as frac
import math as ma
import copy as cp
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()
def gcd(numbers): return func.reduce(frac.gcd, numbers)
def lcm(numbers): return func.reduce(LCM, numbers)
sys.setrecursionlimit(10**7)
mod = 10 ** 9 + 7
inf = np.inf

n,m,r = imap()
cities = map(lambda x: int(x)-1, sinput().split())
abc = np.array([iarr() for i in range(m)])
a,b,c = abc.T[0]-1, abc.T[1]-1, abc.T[2]
graph = sps.csr_matrix((c,(a,b)),(n,n))
wf = sps.csgraph.floyd_warshall(graph,directed=0).astype(int)

anss = []
for city in ite.permutations(cities):
    ans = 0
    for i in range(r-1): ans += wf[city[i]][city[i+1]]
    anss.append(ans)
print(min(anss))
