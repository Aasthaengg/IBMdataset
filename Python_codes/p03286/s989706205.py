#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
if n==0:
    print(0)
    exit()
elif n==1:
    print(1)
    exit()
def check(_n):        
    if _n>0:
        j=0
        while True:
            if pow(2,j)-2*(pow(2,j)-1)//3<=_n<=pow(2,j)+(pow(2,j)-1)//3:
                k=j
                break
            else:
                j+=2
    elif _n<0:
        j=1
        while True:
            if -1*pow(2,j)-2*(pow(2,j-1)-1)//3<=_n<=-1*pow(2,j)+(pow(2,j+1)-1)//3:
                k=j
                break
            else:
                j+=2
    else:
        return 0,0
    return _n-pow(-2,k),k
c=n
ans=0
while True:
    res=check(c)
    if c==0:
        ans+=c
        break
    else:
        ans+=pow(10,res[1])
        c=res[0]
print(ans)
