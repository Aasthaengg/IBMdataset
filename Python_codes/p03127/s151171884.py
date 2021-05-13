# -*- coding: utf-8 -*-
import sys
from math import gcd
from itertools import product
def inpl(): return list(map(int, input().split()))

N = int(input())
A = inpl()
a = A[0]
for b in A[1:]:
    a = gcd(a, b)
print(a)