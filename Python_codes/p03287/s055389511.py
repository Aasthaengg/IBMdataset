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
n,m=map(int,input().split())
a=list(map(int,input().split()))
s=[0]*(n+1)
s[0]=0
for i in range(1,n+1):
    s[i]=s[i-1]+a[i-1]
    s[i]%=m
c=Counter(s)
ans=0
for i in c:
    ans+=(c[i]*(c[i]-1))//2
print(ans)