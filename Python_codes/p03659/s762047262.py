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

n = int(input())
A = list(map(int, input().split()))

acc =[0] * (n + 1)
for i in range(1, n + 1):
    acc[i] = acc[i - 1] + A[i - 1]

ans = INF
for i in range(1, n):
    now = abs(acc[i] - acc[0] - (acc[n] - acc[i]))
    ans = min(ans, now)
print(ans)
