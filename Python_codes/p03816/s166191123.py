import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ni()
A = na()
d = {}
for i in range(N):
    if A[i] not in d.keys():
        d[A[i]] = 0
    else:
        d[A[i]] += 1
s = 0
for k, v in d.items():
    s += v
if s % 2 == 0:
    print(len(d))
else:
    print(len(d) - 1)