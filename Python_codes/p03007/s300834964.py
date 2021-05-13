import bisect
import os
from collections import Counter, deque
from fractions import gcd
from functools import lru_cache
from functools import reduce
import functools
import heapq
import itertools
import math
import numpy as np
import re
import string
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

plus = []
minus = []

for a in A:
    if a >= 0:
        plus.append(a)
    else:
        minus.append(a)
if not plus:
    mm = max(minus)
    plus.append(mm)
    minus.remove(mm)
if not minus:
    mp = min(plus)
    minus.append(mp)
    plus.remove(mp)

hist = []
x = minus.pop()
while len(plus) > 1:
    y = plus.pop()
    hist.append((x, y))
    x = x - y
minus.append(x)

x = plus.pop()
while len(minus) > 1:
    y = minus.pop()
    hist.append((x, y))
    x = x - y
y = minus.pop()
hist.append((x, y))

print(x - y)
for h in hist:
    print(*h)
