from collections import *
from itertools import *
import copy
from heapq import *

S=input()
mod=10**9+7


"""def mpow(x,n):
    num=1
    while n > 0:
        if n&1:
            num=num*x%mod
        x=x*x%mod
        n=n>>1
    return(num)"""

A=0
AB=0
ABC=0
count=0
for s in S:
    if s=="A":
        A+=pow(3,count,mod)
    elif s=="B":
        AB+=A
    elif s=="C":
        ABC+=AB
    else:
        ABC=(ABC*3+AB)%mod
        AB=(AB*3+A)%mod
        A=(A*3+pow(3,count,mod) )%mod
        count+=1
print(ABC%mod)
