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

MOD = 10 ** 4 + 7

N = int(input())
k = 1
while True:
    if N * k % 360 == 0:
        print(k)
        break
    k += 1