# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:35:23 2020

@author: NEC-PCuser
"""
import heapq

N, M = map(int, input().split())
A = [-int(n) for n in input().split(" ")]

heapq.heapify(A)

for i in range(M):
    most_expensive = -heapq.heappop(A)
    most_expensive //= 2
    heapq.heappush(A, -most_expensive)
    
print(-sum(A))