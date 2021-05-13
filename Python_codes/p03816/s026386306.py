#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))
A.sort()

c = Counter(A)
ans = len(c.keys())

if ans%2==0:
    ans -= 1
print(ans)