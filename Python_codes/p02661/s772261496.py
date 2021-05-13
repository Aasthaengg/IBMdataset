
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

n = int(sys.stdin.readline().strip())
a = array1(n)
b = array1(n)

for i in range(n):
    (a[i], b[i]) = list(map(int, sys.stdin.readline().strip().split()))

a = sorted(a)
b = sorted(b)

if n % 2 == 1:
    print(int(b[n//2] - a[n//2] + 1))
else:
    print(int(((b[n//2-1]+b[n//2])/2 - (a[n//2-1]+a[n//2])/2)*2 + 1))

