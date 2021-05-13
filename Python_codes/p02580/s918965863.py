import sys, io, os, re
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from pprint import pprint
from math import sin, cos, pi, radians, sqrt, floor, ceil
from copy import copy, deepcopy
from collections import deque, defaultdict
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
def linc(A, d=1): return list(map(lambda x: x + d, A))
def ldec(A, d=1): return list(map(lambda x: x - d, A))

H, W, M = nn()
T = nm(M)

for i in range(M):
    T[i] = ldec(T[i])

dh = array1(H)
dw = array1(W)

dic = {}

for i in range(M):
    dh[T[i][0]] += 1
    dw[T[i][1]] += 1
    dic[(T[i][0], T[i][1])] = True

dhlist = []
dwlist = []

ansh = max(dh)
for i in range(len(dh)):
    if dh[i] == ansh:
        dhlist.append(i)

answ = max(dw)
for i in range(len(dw)):
    if dw[i] == answ:
        dwlist.append(i)

ans = ansh + answ

for i in dhlist:
    for j in dwlist:
        if (i, j) not in dic:
            print(ans)
            exit(0)

print(ans-1)
