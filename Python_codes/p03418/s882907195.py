#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,K = map(int, input().split())

ans = 0
for b in range(K+1,N+1):
    q = N//b
    r = N%b
    ans += q*(b-K) + max(r-K+1,0)

if K==0:
    ans -= N-K
    
print(ans)