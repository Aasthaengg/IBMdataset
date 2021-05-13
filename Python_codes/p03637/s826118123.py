#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N = int(input())
A = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
cnt4 = 0
for a in A:
    if a%4 == 0:
        cnt4 += 1
    elif a%2 == 0:
        cnt2 += 1
    else:
        cnt1 += 1

if cnt1 <= cnt4:
    print("Yes")
elif cnt1 == cnt4 + 1 and cnt2 == 0:
    print("Yes")
else:
    print("No")