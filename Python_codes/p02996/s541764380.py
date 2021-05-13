import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
ts = []
for i in range(n):
    a, b = map(int, readline().split())
    ts.append((b, a))
ts = sorted(ts, key=lambda x:(x[0], -x[1]))

now = 0
for t in ts:
    now += t[1]
    if now > t[0]:
        print("No")
        exit()
print("Yes")
