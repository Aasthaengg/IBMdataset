#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

s = input()
K = int(input())

N = len(s)

ans = []
for i in range(1,K+1):
    for j in range(N-i+1):
        ans.append(s[j:j+i])

ans = list(set(ans))
ans.sort()
print(ans[K-1])