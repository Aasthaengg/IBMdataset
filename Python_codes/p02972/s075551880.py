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

N = int(readline())
A = list(map(int, readline().split()))

B = [0] * (N + 1)
for i in range(N, 0, -1):
    j = i
    total = 0
    while j <= N:
        total += B[j]
        j += i
    if A[i - 1]:
        if total % 2 == 0:
            B[i] = 1
        else:
            B[i] = 0
    else:
        if total % 2 == 0:
            B[i] = 0
        else:
            B[i] = 1

print(sum(B))
for i in range(len(B)):
    if B[i] == 1:
        print(i)