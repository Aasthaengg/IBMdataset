import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

S = int(input())

x1 = 0
y1 = 0
x2 = -1
y2 = 0
x3 = 1
y3 = -1


# S = abs(x2 * y3 - y2 * x3)
l = round(math.sqrt(S))
x2 = l
y3 = l
while x2 * y3 < S:
    y3 += 1

if x2 * y3 != S:
    y2 = x2 * y3 - S

print(x1, y1, x2, y2, x3, y3)