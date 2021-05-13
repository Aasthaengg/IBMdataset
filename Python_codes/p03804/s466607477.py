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
N, M = map(int, input().split())

A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

def check(x, y):
    for i in range(M):
        for j in range(M):
            if y + i >= N or x + j >= N:
                return False
            if A[y + i][x + j] != B[i][j]:
                return False
    return True

for i in range(N):
    for j in range(N):
        if check(i, j):
            print("Yes")
            exit()
print("No")

