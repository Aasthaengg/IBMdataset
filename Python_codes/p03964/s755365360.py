import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N = int(input())
T = [0]*N
A = [0]*N
for i in range(N):
    T[i],A[i] = map(int,(input().split()))

t,a = T[0],A[0]

for i in range(1,N):
    s = T[i] + A[i]
    now = 1
    l = 1
    r = 10**18//s + 1
    mae = -1
    while now != mae:
        mae = now
        if T[i]*now < t or A[i]*now < a:
            l = now
        else:
            r = now
        now = (l+r+1)//2
    t,a = T[i]*now,A[i]*now
print(t+a)