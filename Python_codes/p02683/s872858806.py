# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:04:57 2020

@author: liang
"""
from operator import add

#import numpy as np
N, M, X = map(int, input().split())

#A = [np.array(list(map(int, input().split()))[1:]) for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
ans = 10**7
for i in range(2**N):
    C_list = list()
    for j in range(N):
        if i>>j&1 == 1:
            C_list.append(j)
    #tmp = np.array( [0]*M )
    tmp = [0]*(M+1)
    for i in C_list:
        tmp = list(map(add, A[i], tmp))
    if all([ i >= X for i in tmp[1:]]) and tmp[0] < ans :
        ans = tmp[0]
    #print(tmp)
if ans == 10**7:
    ans = -1
print(ans)