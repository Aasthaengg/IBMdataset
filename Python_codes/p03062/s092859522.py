import sys
import itertools
# import numpy as np
import time
import math
import heapq
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
INF = 10 ** 9 + 7

# map(int, input().split())
# list(map(int, input().split()))

N = int(input())
A = list(map(int, input().split()))

negs = 0
abs_min = INF
total = 0
for a in A:
    if a < 0:
        negs += 1
    abs_min = min(abs_min, abs(a))
    total += abs(a)

if negs % 2 == 0:
    print(total)
else:
    print(total - abs_min * 2)