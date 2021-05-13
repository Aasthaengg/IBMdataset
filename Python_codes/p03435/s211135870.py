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

C = [0] * 3

for i in range(3):
    C[i] = list(map(int, input().split()))

for i in range(1, 3):
    x = C[i][0] - C[i - 1][0]
    for j in range(1, 3):
        if C[i][j] - C[i - 1][j] != x:
            print("No")
            exit()

for j in range(1, 3):
    x = C[0][j] - C[0][j - 1]
    for i in range(1, 3):
        if C[i][j] - C[i][j - 1] != x:
            print("No")
            exit()
print("Yes")


