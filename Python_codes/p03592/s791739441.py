# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:08:10 2020

@author: NEC-PCuser
"""

N, M, K =  map(int, input().split())
ans = "No"
for i in range(0, N + 1):
    for j in range(0, M + 1):
        kosu = i * M - 2 * j * i + j * N
        if (kosu == K):
            ans = "Yes"
            break
    else:
        continue
    break
print(ans)