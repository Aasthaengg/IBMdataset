#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N,M = map(int, input().split())

if N <= M//2:
    ans = N + max(M-2*N,0)//4
else:
    ans = M // 2

print(ans)