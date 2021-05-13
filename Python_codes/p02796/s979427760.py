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
A = [0] * N
for i in range(N):
    x, l = map(int, input().split())
    A[i] = (x - l, x + l)
A = sorted(A, key=lambda x: x[1])

last = -INF
ans = 0
for l, r in A:
    if l < last:
        continue
    ans += 1
    last = r
print(ans)
    

