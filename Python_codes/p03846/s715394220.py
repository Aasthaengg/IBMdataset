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

X = [0] * N
for i, a in enumerate(A):
    j = (N - 1 - a) // 2
    X[j] += 1

for i, x in enumerate(X):
    if x == 1 and not (i == (N + 1) // 2 - 1):
        print(0)
        exit()
    if x > 2:
        print(0)
        exit()

ans = 1
for x in X:
    if x == 0:
        break
    ans *= x
    ans %= MOD
print(ans)

