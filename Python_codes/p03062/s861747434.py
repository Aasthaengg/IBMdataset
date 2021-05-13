# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:59:38 2020

@author: NEC-PCuser
"""

N = int(input())
A = list(map(int, input().split()))
minusCount = 0
ans = 0
miniumAbs = 10 ** 9
for i in range(0, len(A)):
    if (A[i] < 0):
        minusCount += 1
    if (miniumAbs > abs(A[i])):
        miniumAbs = abs(A[i])
    ans += abs(A[i])
if minusCount %2 == 0:
    print(ans)
else:
    print(ans - 2 * miniumAbs)