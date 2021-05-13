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

N, M = map(int, input().split())
A = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A[a] += 1
    A[b] += 1

for a in A:
    if a % 2 == 1:
        print("NO")
        break
else:
    print("YES")