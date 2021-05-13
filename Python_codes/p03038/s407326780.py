# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:42:06 2020

@author: NEC-PCuser
"""

import heapq

N, M = map(int, input().split())

A = list(map(int, input().split()))

B_C = []
for i in range(M):
    b_c = list(map(int, input().split()))
    B_C.append(b_c)
 
B_C = sorted(B_C, reverse=True, key=lambda x: x[1])
ans = sum(A)
heapq.heapify(A)
i = 0 

while True:
    for j in range(B_C[i][0]):
        c = heapq.heappop(A)
        ans -= c
        if c < B_C[i][1]:
            heapq.heappush(A, B_C[i][1])
            ans += B_C[i][1]
        else:
            heapq.heappush(A, c)
            ans += c
            break
    else:
        i += 1
        if (len(B_C) == i):
            break
        continue
    break

print(ans)
