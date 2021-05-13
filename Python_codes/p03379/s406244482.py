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
X = list(map(int, input().split()))

A = sorted(X)

med1 = A[N // 2 - 1] 
med2 = A[N // 2]

for i, x in enumerate(X):
    if x <= med1:
        print(med2)
    else:
        print(med1)