# -*- encoding: utf-8 -*-
import sys
import re
import random
import numpy as np
from math import sqrt,log
from fractions import gcd  # python<=3.4
from collections import Counter, defaultdict

# st = Counter(raw_input())

MOD=1000000007

def lcm(a,b):
  return a/gcd(a,b)*b


def read_ints():
  return map(int, input().split())


def calc_kmax(az,bz):
    assert az < bz

    lo = 0    # ng
    hi = az # ok
    while lo+1 < hi:
        k = (lo + hi)//2
        if k * bz >= (k+1) * az:
            hi = k
        else:
            lo = k
    return hi


def solve(T1,T2,A1,A2,B1,B2):
    T = T1 + T2
    az = T1*A1 + T2*A2
    bz = T1*B1 + T2*B2
    if az == bz:
        print('infinity')
        return False
    if az > bz:
        A1,A2,B1,B2 = B1,B2,A1,A2
        az,bz = bz,az

    numer = T1*(A1-B1)
    denom = (bz-az)

    g = numer / denom
    gi = int(g)
    gr = gi - g

    if (g > 0):
        if gr == 0:
            ans = -1 + gi*2 + 1
        else:
            ans = -1 + (gi+1)*2
    else:
        ans = 0

    print(ans)


T1,T2 = read_ints()
A1,A2 = read_ints()
B1,B2 = read_ints()
solve(T1,T2, A1,A2, B1,B2)
