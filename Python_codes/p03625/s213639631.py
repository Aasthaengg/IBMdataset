import sys
#import numpy as np
import math
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
from fractions  import gcd

#input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.sort()
res=a.pop()
ans=[]
while a:
    l=a.pop()
    if res==l:
        ans.append(l)
        if a:
            res=a.pop()
        else:
            break
    else:
        res=l
    if len(ans)==2:
        break
if len(ans)<2:
    print(0)
else:
    print(ans[0]*ans[1])