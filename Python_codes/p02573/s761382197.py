import sys, io, os, re
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from pprint import pprint
from math import sin, cos, pi, radians, sqrt, floor, ceil
from copy import copy, deepcopy
from collections import deque, defaultdict
from fractions import gcd
from functools import reduce
from itertools import groupby, combinations
from heapq import heapify, heappush, heappop

#sys.setrecursionlimit(30000)

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

N, M = nn()
T = nm(M)

for i in range(M):
    T[i][0] -= 1
    T[i][1] -= 1

dic = defaultdict(list)

m = {}
for i in range(M):
    if (T[i][0], T[i][1]) in m:
        continue
    m[(T[i][0], T[i][1])] = True
    dic[T[i][0]].append(T[i][1])
    dic[T[i][1]].append(T[i][0])

def search(n):
    ret = 1
    deq = deque()

    memo[n] = 1
    for t in dic[n]:
        if memo[t] == 0:
            memo[t] = 1
            deq.append(t)

    while len(deq) != 0:
        d = deq.pop()
        ret += 1
        for t in dic[d]:
            if memo[t] == 0:
                memo[t] = 1
                deq.append(t)

    return ret

memo = array1(N)

ans = 0
for i in range(N):
    if memo[i] == 1:
        continue

    ans = max(search(i), ans)

print(ans)