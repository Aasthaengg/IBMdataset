# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:32:21 2020

@author: Kanaru Sato
"""

n,d = list(map(int, input().split()))

ans = (n+(2*d+1)-1)//(2*d+1)

print(ans)