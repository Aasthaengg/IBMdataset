import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


N,K = map(int,input().split())
W = []
for _ in range(N):
    W.append(int(input()))


def is_OK(P):
    track_index = 0
    w_index = 0
    while w_index < N and track_index < K:
        tmp_sum = 0
        while  w_index < N and tmp_sum+W[w_index] <= P:
            tmp_sum += W[w_index]
            w_index += 1
        track_index += 1
    return w_index == N

L = 0
R = 100000*100000
mid = (L+R)//2
ans = R

while L <= R:
    if is_OK(mid):
        ans = mid
        R = mid-1
    else:
        L = mid+1
    mid = (L+R)//2

print("%d"%ans)


