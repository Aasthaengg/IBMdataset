import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

a = ri()
b = ri()
c = ri()
x = ri()
cnt = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i*500 + j*100 + k*50 == x:
                cnt += 1
print(cnt)












