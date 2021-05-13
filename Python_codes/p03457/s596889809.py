import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N = int(input())
px, py, pt = 0, 0, 0
ok = True
for i in range(N):
    t, x, y = map(int, input().split())
    diff = abs((x + y) - (px + py)) 
    if diff > t - pt:
        ok = False
    if diff % 2 != (t - pt) % 2:
        ok = False
    px = x
    py = y
    pt = t

if ok:
    print("Yes")
else:
    print("No")