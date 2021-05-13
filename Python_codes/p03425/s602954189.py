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

# map(int, input().split())
# list(map(int, input().split()))

N = int(input())
S = [0] * N
count = [0] * 5
for i in range(N):
    S[i] = input()
    if S[i][0] == 'M':
        count[0] += 1
    if S[i][0] == 'A':
        count[1] += 1
    if S[i][0] == 'R':
        count[2] += 1
    if S[i][0] == 'C':
        count[3] += 1
    if S[i][0] == 'H':
        count[4] += 1

ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += count[i] * count[j] * count[k] 
print(ans)
