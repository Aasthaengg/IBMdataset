#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

W = H = 0
L = sorted(list(Counter(A).items()),key=lambda x:(-x[0]))
for k,v in L:
    if W == 0:
        if v >= 4:
            W = H = k
            break
        elif v >= 2:
            W = k
    elif H == 0:
        if v >= 2:
            H = k
            break

print(H*W)