import sys
#import numpy as np
#import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
res=0
for i in range(n-1):
    s=a[i]+a[i+1]
    if s>x:
        a[i+1]-=(s-x)
        res+=(s-x)
        if a[i+1]<0:
            a[i+1]=0
print(res)