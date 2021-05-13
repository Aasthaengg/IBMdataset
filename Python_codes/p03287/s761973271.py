#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,M = map(int, input().split())
A = list(map(int, input().split()))

Asum = [0]
for a in A:
    Asum.append(Asum[-1]+a)

for i in range(N+1):
    Asum[i] %= M
Asum.sort()

ans = 0
for c in Counter(Asum).values():
    ans += c*(c-1)//2

print(ans)