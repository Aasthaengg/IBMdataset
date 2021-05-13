#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n,m=map(int,input().split())
d={i:0 for i in range(1,m+1)}
for i in range(n):
    a=list(map(int,input().split()))
    k=a[0]
    for j in range(k):
        d[a[j+1]]+=1
ans=0
for i in d.keys():
    if d[i]==n:
        ans+=1
print(ans)