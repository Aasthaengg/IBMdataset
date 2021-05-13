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

N, K = map(int, input().split())
X = list(map(int, input().split()))

left = 0
right = K - 1

ans = INF
while right < len(X):
    val1 = abs(X[left]) + abs(X[right] - X[left])
    val2 = abs(X[right]) + abs(X[right] - X[left])
    ans = min(ans, val1, val2)
    left += 1
    right += 1
print(ans)