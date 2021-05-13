import collections
import numpy as np
import sys
import copy
from functools import lru_cache
sys.setrecursionlimit(10**8)
#N,K=map(int,input().split())
#N=int(input())
#h=np.array(list(map(int,input().split())))
#ans=0
num2alpha = lambda c: chr(c+96)
s=list(input())
ans=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        ans+=1
print(ans)