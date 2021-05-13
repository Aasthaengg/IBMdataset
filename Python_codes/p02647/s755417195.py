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
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
while True:
    b=[0]*n
    if c==k:
        break
    for i in range(n):
        l=max(i-a[i],0)
        r=min(n-1,i+a[i])
        b[l]+=1
        if r+1<n:
            b[r+1]-=1
    f=True
    if b[0]!=n:
        f=False
    for i in range(1,n):
        b[i]+=b[i-1]
        if b[i]!=n:
            f=False
    a=b
    c+=1
    if f:
        break
print(*a)
