import math
import collections
from operator import mul
from functools import reduce
import bisect

#n,m=map(int,input().split())

s=input()
k=int(input())
a=[]
for i in range(len(s)):
    for j in range(i+1,min(i+2+k,len(s)+1)):
        a.append(s[i:j])
a=sorted(list(set(a)))
print(a[k-1])







