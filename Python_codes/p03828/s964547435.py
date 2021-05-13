#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

MOD = 10**9+7
N = int(input())

pf = [0]*(N+1)
for n in range(2,N+1):
    q = n
    i = 2
    while q>1:
        if q%i == 0:
            pf[i] += 1
            q /= i
        else:
            i += 1

ans = 1
for f in pf:
    ans = (ans*(f+1))%MOD

print(ans)