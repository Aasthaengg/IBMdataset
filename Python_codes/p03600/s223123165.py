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

# map(int, input().split())
# list(map(int, input().split()))

N = int(input())
dist = [[float("inf") if i != j else 0 for i in range(N)] for j in range(N)]

for i in range(N):
    dist[i] = list(map(int, input().split()))

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                exit()

for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if k == i or k == j:
                continue
            if dist[i][j] == dist[i][k] + dist[k][j]:
                break
        else:
            ans += dist[i][j]
print(ans)