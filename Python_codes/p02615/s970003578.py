# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:47:07 2020

@author: ezwry
"""
import math

n=int(input())
a=list(map(int,input().split()))

a.sort(reverse=1)

ans=[]

for i in range(n-1):
    jyun=math.ceil(i/2)
    ans.append(a[jyun])

answer=sum(ans)
print(answer)