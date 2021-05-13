#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
m=int(input())
def factorize(n):
    fct={}
    temp=n
    if temp<4:
        fct[temp]=1
    else:
        e=0
        while temp%2==0:
            temp=temp//2
            e+=1
        if e>0:
            fct[2]=e
    
    for b in range(3,int(n**0.5)+1,2):
        e=0
        while temp%b == 0:
            temp=temp//b
            e+=1
        if e>0:
            fct[b]=e
    if temp!=1:
        fct[temp]=1
    return fct
res={}
for i in range(2,m+1):
    f=factorize(i)
    for j in f:
        if j not in res:
            res[j]=f[j]
        else:
            res[j]+=f[j]
ans=1
for i in res.values():
   
    ans*=(i+1)
print(ans%(10**9+7))