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

N, X = map(int, input().split())
H = [0] * N
for i in range(N):
    H[i] = int(input())

H = sorted(H)

left = 0
right = X
ans = INF
while right <= N:
    mn = H[left]
    mx = H[right - 1]
    ans = min(ans, mx - mn)
    left += 1
    right += 1
print(ans)

