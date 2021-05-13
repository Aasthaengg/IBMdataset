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

S = sum(A)

x = [0] * N
x[0] = S - 2 * sum(A[i] for i in range(N) if i % 2 == 1)

for i in range(1, N):
    x[i] = 2 * A[i - 1] - x[i - 1]
for i in x:
    print(i)