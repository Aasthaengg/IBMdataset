import sys
import itertools
# import numpy as np
import time
import math
import heapq
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
INF = 10 ** 9 + 7

# map(int, input().split())
# list(map(int, input().split()))

N, K = map(int, input().split())

big_array = [0] * (10 ** 5 + 1)
for i in range(N):
    a, b = map(int, input().split())
    big_array[a] += b

count = 0
for i in range(1, 10 ** 5 + 1):
    count += big_array[i]
    if count >= K:
        print(i)
        break


