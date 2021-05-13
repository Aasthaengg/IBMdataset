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
import bisect
n=int(input())
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
dic={}
for i in range(2,n+1):
    d=factorize(i)
    for j in d:
        if j not in dic:
            dic[j]=d[j]
        else:
            dic[j]+=d[j]
n2=0
n4=0
n24=0
n14=0
n74=0
for i in dic:
    if dic[i]>=4:
        n4+=1
    if dic[i]>=2:
        n2+=1
    if dic[i]>=14:
        n14+=1
    if dic[i]>=24:
        n24+=1
    if dic[i]>=74:
        n74+=1
ans=((n4*(n4-1))//2)*(n2-2)+((n4-1)*n14)+((n2-1)*n24)+n74
print(ans)