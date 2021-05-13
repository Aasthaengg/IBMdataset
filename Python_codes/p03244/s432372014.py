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
v=list(map(int,input().split()))
even={}
odd={}
for i in range(n):
    if i%2==0:
        if v[i] not in even:
            even[v[i]]=1
        else:
            even[v[i]]+=1
    else:
        if v[i] not in odd:
            odd[v[i]]=1
        else:
            odd[v[i]]+=1
    
even=sorted(even.items(),key=lambda x: x[1],reverse=True)
odd=sorted(odd.items(),key=lambda x:x[1],reverse=True)
if even[0][0]==odd[0][0]:
    e1=even[0][1]
    e2=even[1][1] if len(even)>1 else 0
    o1=odd[0][1]
    o2=odd[1][1] if len(odd)>1 else 0
    print(min((n-e1-o2),(n-e2-o1)))
else:
    e=even[0][1]
    o=odd[0][1]
    print(n-e-o)
