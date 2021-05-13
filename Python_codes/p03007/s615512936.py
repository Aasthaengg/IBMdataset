import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
#from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
M=max(a)
m=min(a)
resm=m
resM=M
c_M=False
c_m=False
ans=[]
for i in range(n):
    if a[i]==M and c_M==False:
        c_M=True
        continue
    elif a[i]==m and c_m==False:
        c_m=True
        continue
    if a[i]>0:
        ans.append((resm,a[i]))
        resm=resm-a[i]
    else:
        ans.append((resM,a[i]))
        resM=resM-a[i]
print(resM-resm)
for i in ans:
    print(*i)
print(resM,resm)
