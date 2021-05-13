import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

input=sys.stdin.readline
x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ab=[0]*(x*y)
c.sort(reverse=True)
for i in range(x):
    for j in range(y):
        ab[y*i+j]=a[i]+b[j]
ab.sort(reverse=True)
d=ab[:k]
ans=[0]*(k*z)
for i in range(len(d)):
    for j in range(z):
        ans[z*i+j]=d[i]+c[j]
ans.sort(reverse=True)
for i in range(k):
    print(ans[i])