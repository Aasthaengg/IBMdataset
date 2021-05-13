#!/usr/bin/env python

from collections import deque, defaultdict
import itertools as ite
import sys
import math
import decimal

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7
X, Y = map(int, raw_input().split())
ans = max(4 - X, 0) * 100000 + max(4 - Y, 0) * 100000
if X * Y == 1:
    ans += 400000
print ans