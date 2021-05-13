# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)
def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]

def nck(n, k, mod):
    bunbo = bunshi = 1
    for i in range(k):
        bunshi = (bunshi * (n-i)) % mod
        bunbo = (bunbo * (i+1)) % mod
    return (bunshi * pow(bunbo, mod-2, mod)) % mod

N = z()
s = []
M,A,R,C,H = 0, 0, 0, 0, 0
for i in range(N):
    tmp = S()
    if (tmp[0] == 'M'):
        M+=1
    elif (tmp[0] == 'A'):
        A+=1
    elif (tmp[0] == 'R'):
        R+=1
    elif (tmp[0] == 'C'):
        C+=1
    elif (tmp[0] == 'H'):
        H+=1
ans = M*A*R + M*A*C + M*A*H + M*R*C + M*R*H \
     + M*C*H + A*R*C + A*C*H + R*C*H+ A*R*H
print(ans)