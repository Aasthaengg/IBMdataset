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
A = list(map(int, input().split()))
avg = sum(A) / N

d = INF
ans = 0
for i in range(N):
    diff = abs(A[i] - avg)
    if diff < d:
        d = diff
        ans = i
print(ans)
