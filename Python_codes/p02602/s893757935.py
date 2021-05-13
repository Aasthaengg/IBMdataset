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
A = list(map(int, input().split()))

for i in range(K, N):
    if A[i] > A[i - K]:
        print("Yes")
    else:
        print("No")