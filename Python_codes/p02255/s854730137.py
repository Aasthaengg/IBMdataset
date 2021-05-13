#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()
n=int(raw_input())
a=map(int,raw_input().split())
ans=chk=0
def prin(l):
    for i in l:
        print i,
    print

prin(a)
for i in range(1,n):
    v=a[i]
    j=i-1
    while(j>=0 and a[j]>v):
        a[j+1]=a[j]
        j-=1
    a[j+1]=v
    prin(a)