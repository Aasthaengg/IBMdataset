# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = list(map(int,readline().split()))

ans1 = 0
ans2 = 0
S1 = 0
S2 = 0
# 偶数項-,奇数項を+にする
for i in range(N):
    S1 += A[i]
    S2 += A[i]
    if i & 1: 
        if S1 >= 0:
            ans1 += S1+1
            S1 = -1
        if S2 <= 0:
            ans2 += 1-S2
            S2 = 1
    else: 
        if S1 <= 0:
            ans1 += 1-S1
            S1 = 1
        if S2 >= 0:
            ans2 += S2+1
            S2 = -1
print(min(ans1,ans2))   