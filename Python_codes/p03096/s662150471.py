# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:36:58 2019

@author: Yamazaki Kenichi
"""

N = int(input())
C = [int(input()) for i in range(N)]
mod = 10**9+7
T = [[0] for i in range(2*10**5+1)]
ans = [1 for i in range(N+1)]
for i in range(N): 
    if i == 0 or C[i] != C[i-1]:
        T[C[i]][0] += 1
        T[C[i]].append(i)
        if T[C[i]][0] >=2:
            ans[i] = (ans[i-1] + ans[T[C[i]][-2]])%mod
        else:
            ans[i] = ans[i-1]%mod
    else:
        ans[i] = ans[i-1]%mod
        
print(ans[N-1]%mod)