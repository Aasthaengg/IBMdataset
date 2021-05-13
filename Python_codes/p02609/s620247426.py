import sys, io, os, re
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from pprint import pprint
from math import sin, cos, pi, radians, sqrt, floor, ceil
from copy import copy, deepcopy
from collections import deque
from fractions import gcd
from functools import reduce
from itertools import groupby
from heapq import heapify, heappush, heappop

# sys.setrecursionlimit(5000)

n1 = lambda: int(sys.stdin.readline().strip())
nn = lambda: list(map(int, sys.stdin.readline().strip().split()))
f1 = lambda: float(sys.stdin.readline().strip())
fn = lambda: list(map(float, sys.stdin.readline().strip().split()))
s1 = lambda: sys.stdin.readline().strip()
sn = lambda: list(sys.stdin.readline().strip().split())
nl = lambda n: [n1() for _ in range(n)]
fl = lambda n: [f1() for _ in range(n)]
sl = lambda n: [s1() for _ in range(n)]
nm = lambda n: [nn() for _ in range(n)]
fm = lambda n: [fn() for _ in range(n)]
sm = lambda n: [sn() for _ in range(n)]

def array1(n, d=0): return [d] * n
def array2(n, m, d=0): return [[d] * m for x in range(n)]
def array3(n, m, l, d=0): return [[[d] * l for y in xrange(m)] for x in xrange(n)]
def linc(A, d=1): return map(lambda x: x + d, A)
def ldec(A, d=1): return map(lambda x: x - d, A)

popcount = lambda x: bin(x).count("1")
bitflip = lambda x, n: x ^ (1 << n)
bitflip2 = lambda x, n: x ^ (1 << (len(bin(x))-2 - (n+1)))
bits = lambda x, n = 0: bin(x)[2:].zfill(n)

N = n1()
X = list(map(int, list(s1())))

rt = [0, 0]
t1 = 1
t2 = 1
p = X.count(1)

for i in range(N-1, -1, -1):    
    if X[i] == 1:
        if p > 1: rt[0] = (rt[0] + t1) % (p - 1)
        rt[1] = (rt[1] + t2) % (p + 1)
    if p > 1: t1 = t1 * 2 % (p - 1)
    t2 = t2 * 2 % (p + 1)

for i in range(N):
    if X[i] == 1 and p == 1:
        print(0)
        continue

    if X[i] == 0:
        t = (rt[1] + pow(2, N-i-1, p+1)) % (p + 1)
    else:
        t = (rt[0] - pow(2, N-i-1, p-1)) % (p - 1)

    ans = 1
    while t > 0:
        t %= popcount(t)
        ans += 1
    
    print(ans)