
import sys, io, os, re
import bisect
from pprint import pprint
from math import sin, cos, pi, radians, sqrt, floor
from copy import copy, deepcopy
from collections import deque
from fractions import gcd
from functools import reduce

def array1(n): return [0] * n
def array2(n, m): return [[0] * m for x in range(n)]
def array3(n, m, l): return [[[0] * l for y in xrange(m)] for x in xrange(n)]

n, s = list(map(int, sys.stdin.readline().strip().split()))
a = [0 for x in range(n)]
a = list(map(int, sys.stdin.readline().strip().split()))

mod = 998244353

d = array2(n+1, s+1)
d[0][0] = 1

for i in range(n):
    #print(d)
    for j in range(s+1):
        d[i+1][j] += d[i][j] * 2
        d[i+1][j] %= mod
        if j + a[i] <= s:
            d[i+1][j+a[i]] += d[i][j]
            d[i+1][j+a[i]] %= mod

#print(d)
print(d[n][s])
