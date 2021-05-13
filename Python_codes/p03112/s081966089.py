# -*- coding: utf-8 -*-
#D - Lazy Faith
import sys
from bisect import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
A, B, Q = map(int, readline().split())
INF = 10**31
S = [-INF]
for _ in range(A):
    s = int(readline())
    S.append(s)
S.append(INF)
T = [-INF]
for _ in range(B):
    t = int(readline())
    T.append(t)
T.append(INF)

for _ in range(Q):
    x = int(readline())
    ind_s = bisect(S,x)
    ind_t = bisect(T,x)
    s1,s2 = S[ind_s-1],S[ind_s]
    t1,t2 = T[ind_t-1],T[ind_t]
    d1 = (x-s1) + (t2-s1) if x-s1 < t2-x else (t2-x) + (t2-s1)
    d2 = (x-t1) + (s2-t1) if x-t1 < s2-x else (s2-x) + (s2-t1)
    d3 = x-s1 if s1 < t1 else x-t1
    d4 = t2-x if s2 < t2 else s2-x
    ans = min(d1,d2,d3,d4)
    print(ans)    