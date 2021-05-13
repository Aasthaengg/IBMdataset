# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:15:13 2020

@author: NEC-PCuser
"""

N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    A.append(input())

for i in range(M):
    B.append(input())

result = "No" 
for i in range(N - M + 1):
    for j in range(N - M + 1):
        for k in range(M):
            for l in range(M):
                if (A[i + k][j + l] != B[k][l]):
                    break
            else:
                continue
            break
        else:
            result = "Yes"
            break

print(result)