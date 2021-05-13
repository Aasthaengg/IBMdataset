# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:52:36 2020

@author: shinba
"""

n,m = map(int,input().split())

ans = 0

if n >= 2 and m >= 2:
    ans += (n-2)*(m-2)
else:
    if n == 1 and m == 1:
        ans = 1
    else:
        ans = max(m,n) - 2
    
print(ans)
