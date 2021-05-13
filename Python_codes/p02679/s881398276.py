
import sys, io, os, re
import bisect
from pprint import pprint
from math import sin, cos, pi, radians, sqrt, floor, ceil
from copy import copy, deepcopy
from collections import deque, defaultdict
from fractions import gcd
from functools import reduce

def array1(n): return [0] * n
def array2(n, m): return [[0] * m for x in range(n)]
def array3(n, m, l): return [[[0] * l for y in xrange(m)] for x in xrange(n)]

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

mod = 1000000007

N = n1()
(A, B) = ([], [])
for i in range(N):
    a, b = nn()
    g = gcd(a, b)
    if g != 0: a //= g; b //=g
    A.append(a)
    B.append(b)

d = defaultdict(int)
for i in range(N):
    d[(A[i], B[i])] += 1

ans = 1
n = 0
if (0, 0) in d:
    n = d.pop((0, 0))

while len(d) > 0:
    #print(d, ans)
    (x, y), n1 = d.popitem()
    if y < 0: x *= -1; y *= -1

    n2 = 0
    if (y, -x) in d: n2 += d.pop((y, -x))
    if (-y, x) in d: n2 += d.pop((-y, x))

    ans = (ans * ((pow(2,n1,mod) -1 + pow(2,n2,mod) - 1) % mod + 1)) % mod

print((ans-1+n)%mod)