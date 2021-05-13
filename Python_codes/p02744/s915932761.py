import collections
import numpy as np
import sys
import copy
from functools import lru_cache


sys.setrecursionlimit(10**8)
#N,K=map(int,input().split())
N=int(input())
#h=np.array(list(map(int,input().split())))
#ans=0
num2alpha = lambda c: chr(c+96)


def dfs(K,b,s):
    if len(s)==N:
        return b.append(s)
        s=""
    elif len(s)>N:
        return
    elif len(s)<N:
        x = copy.deepcopy(s)
        for i in range(N):
            if i+1-len(set(x))< 2:
                s=x+num2alpha(i+1)
                dfs(N-1, b, s)
B=list()
m=""
dfs(N-1,B,m)
for i in B:
    print(i)
