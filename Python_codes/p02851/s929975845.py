import sys
import math
from itertools import accumulate as acc

def func(s):
    return (int(s)-1)%K


N,K=map(int,input().split())
a=list(map(int,input().split()))
x=[0]
tmp=0
for i in range(N):
    tmp=(tmp+a[i]-1)%K
    x+=[tmp]
dic={}
ans=0
if N<K:
    for i in range(N+1):
        if x[i] in dic: dic[x[i]]+=1
        else: dic[x[i]]=1
    for i in dic:
        ans+=dic[i]*(dic[i]-1)//2

    
else:
    for i in range(K):
        p=x[i]
        if p in dic: dic[p]+=1
        else: dic[p]=1
        ans+=dic[p]-1
    for i in range(K,N+1):
        p=x[i]
        if p in dic: dic[p]+=1
        else: dic[p]=1
        dic[x[i-K]]-=1
        ans+=dic[p]-1

print(ans)