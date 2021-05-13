#!/usr/bin/env python3
# sys.stdin.readline()
import numpy as np
import sys
import math
input = sys.stdin.readline
n,c,k = map(int,input().split())
A = [int(input()) for i in range(n)]
a = sorted(A)
ans = 0
time = 0.1 
num = 0
for i in range(n):
    if ans == 0:
        ans +=1
        time = a[0] 
        num +=1
    elif ans != 0 and a[i] <= time +k and num < c :
        num +=1
    elif  ans != 0 and (c <=num  or  time +k <=a[i]):
      
        time = a[i] 
        num = 1
        ans +=1
print(ans)