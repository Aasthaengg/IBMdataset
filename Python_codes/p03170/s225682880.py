# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:52:57 2020

@author: over-
"""


N, K=map(int,input().split())
a=input().split()
a=[int(i) for i in a]
a.sort()

dp=[0]*(K+1)
dp[0]=1

for i in range(1,K+1):
    dp[i]=1
    for j in a:
        if j > i: break
        if dp[i-j]==1: 
            dp[i]=0
            break
          
            

    
if dp[-1]==0:
    print('First')
else:
    print('Second')
        
        
        



