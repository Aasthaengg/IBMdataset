# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:18:43 2020

@author: shinba
"""

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

r,g,b,n = map(int,input().split())
ans = 0

for i in range(n+1):
    for j in range(n+1):
        if is_integer_num((n-i*r-j*g)/b) and 0 <= n-i*r-j*g:
            ans += 1

print(ans)
            
