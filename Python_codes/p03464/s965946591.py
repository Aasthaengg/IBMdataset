# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np
import sys

def IMPOSSIBLE():
    print(-1)
    sys.exit()
    

k = int(input())
a = list(map(int,input().split()))[::-1]
min_num = 2
max_num = 3

if(a[0]!=2):IMPOSSIBLE()

for i in range(len(a)-1):
    if(a[i+1] > max_num):IMPOSSIBLE()
    else:
        min_num = a[i+1]*(min_num//a[i+1] if min_num%a[i+1]==0 else min_num//a[i+1]+1)
        max_num = a[i+1]*((max_num//a[i+1])+1)-1
        

tmpmin = min_num
tmpmax = max_num
for i in range(len(a)):
    tmpmin -= tmpmin%a[len(a)-i-1]
    tmpmax -= tmpmax%a[len(a)-i-1]
if(tmpmin != 2 or tmpmax != 2):IMPOSSIBLE()
    
print(str(min_num)+' '+str(max_num))