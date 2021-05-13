# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 05:49:43 2020

@author: Dell
"""

n = int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
for i in range(n):
    
    
   
    
    
    
    if a[i]>0:
        k=min(a[i],b[i])
        s+=k
        b[i]-=k
        a[i]-=k
    if b[i]>0:
        if a[i+1]>0:
            k=min(a[i+1],b[i])
            s+=k
            b[i]-=k
            a[i+1]-=k
print(s)
    

    
