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

N = int(input())
A = list(map(int, input().split()))

x = max(A)
A = list(filter(lambda a: a != x, A))
med = x / 2

num = INF
y = 0
for a in A:
    if abs(med - a) < num:
        num = abs(med - a)
        y = a
print(x, y)
