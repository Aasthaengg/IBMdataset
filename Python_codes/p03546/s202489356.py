import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
# list(map(int, input().split()))

H, W = map(int, input().split())

C = [0] * 10
for i in range(10):
    C[i] = list(map(int, input().split()))

A = [0] * H
for i in range(H):
    A[i] = list(map(int, input().split()))

for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][k] + C[k][j], C[i][j])

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1 or A[i][j] == 1:
            continue
        ans += C[A[i][j]][1]
print(ans)

