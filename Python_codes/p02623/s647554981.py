from collections import defaultdict, deque
import sys
import heapq
import bisect
import itertools
import queue
import copy
import time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())

def inpl(): return list(map(int, sys.stdin.readline().split()))

def inpl_str(): return list(sys.stdin.readline().split())

N, M, K = inpl()
A = [0]
B = [0]
A += inpl()
B += inpl()
for i in range(N):
    A[i+1] += A[i]
for i in range(M):
    B[i+1] += B[i]

ans = 0
j = M
for i in range(N+1):
    if A[i] > K:
        break
    while B[j] > K - A[i]:
        j -= 1
    ans = max(ans, i+j)
print(ans)