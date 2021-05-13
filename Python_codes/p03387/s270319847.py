# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:44:27 2020

@author: liang
"""

A, B, C = map(int, input().split())

if A > B:
    if B > C:
        m1,m2,m3 = A, B, C
    else:
        if A > C:
            m1,m2,m3 = A, C, B
        else:
            m1,m2,m3 = C, A, B
else:
    if A > C:
        m1,m2,m3 = B, A, C
    else:
        if B > C:
            m1,m2,m3 = B, C, A
        else:
            m1,m2,m3 = C, B, A
ans = 0
ans += m1 - m2
ans += (m2-m3)//2
if (m2-m3)%2 == 1:
    ans += 2
print(ans)