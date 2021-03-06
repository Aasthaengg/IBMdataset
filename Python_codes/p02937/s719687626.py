#!/usr/bin/env python3
 
import sys
# 以下を記述しないとTLEになる, 何故？
from heapq import heappushpop, heapify, heapreplace
from collections import defaultdict
# ---- ここまで -----------------------
 
S = input()
T = input()
lenS = len(S)
lenT = len(T)
F1 = [False]*26
F2 = [False]*26
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(lenS):
    F1[alpha.index(S[i])] = True
for i in range(lenT):
    F2[alpha.index(T[i])] = True
for i in range(26):
    if not F1[i] and F2[i]:
        print(-1)
        sys.exit()
 
ind = S.index(T[0])
ans = ind+1
for i in range(1,lenT):
    S = S[ind+1:] + S[:ind+1]
    ind = S.index(T[i])
    ans += ind+1
 
print(ans)