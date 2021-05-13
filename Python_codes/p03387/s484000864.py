# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:06:24 2020

@author: liang
"""
num = [int(x) for x in input().split()]
M = max(num)
S = sum(num)
if M*3%2 == S%2:
    print((3*M-S)//2)
else:
    print((3*(M+1)-S)//2)