#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

N,T = map(int, input().split())
A = list(map(int, input().split()))

Amin = [A[0]] + [0]*(N-1)
for i in range(1,N):
    if A[i] < Amin[i-1]: Amin[i] = A[i]
    else: Amin[i] = Amin[i-1]

B = A[0] - Amin[0]
for i in range(1,N): B = max(B, A[i]-Amin[i])

ans = 0
for i in range(N):
    if A[i] - Amin[i] == B:
        ans += 1

print(ans)