# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:50:04 2020

@author: NEC-PCuser
"""

N, K = map(int, input().split())
ab_list = []
for i in range(N):
    a, b = map(int, input().split())
    ab_list.append([a,b])

ab_list.sort()


count = 0
for i in range(0, N):
    count += ab_list[i][1]
    
    if (count >= K):
        print(ab_list[i][0])
        break
