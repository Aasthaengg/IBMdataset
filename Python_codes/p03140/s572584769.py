#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18

N = input()
A = raw_input()
B = raw_input()
C = raw_input()

ans = 0
for i in range(N):
    m = {A[i], B[i], C[i]}
    ans += len(m) - 1

print ans