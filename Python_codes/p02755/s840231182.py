import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
A, B = map(int, input().split())

for i in range(1, 1010):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        break
else:
    print(-1)