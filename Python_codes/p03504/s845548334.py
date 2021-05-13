#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

N,C = map(int, input().split())
L = [list(map(int, input().split())) for i in range(N)]

T_MAX = 10**5
time = [[0]*C for i in range(T_MAX)]

for s,t,c in L:
    time[s-1][c-1] += 1
    time[t-1][c-1] -= 1
 
ans = 0
tmp = 0
for i in range(T_MAX):
    tmp += time[i].count(1)
    ans = max(ans,tmp)
    tmp -= time[i].count(-1)

print(ans)