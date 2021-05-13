# coding: utf-8
import re
import math
import fractions
import random
from heapq import heappop,heappush
import time
import sys
input = sys.stdin.readline
#import numpy as np
mod=int(10**9+7)
inf=int(10**20)
class union_find():
    def __init__(self,n):
        self.n=n
        self.P=[a for a in range(N)]
        self.rank=[0]*n
 
    def find(self,x):
        if(x!=self.P[x]):self.P[x]=self.find(self.P[x])
        return self.P[x]
 
    def same(self,x,y):
        return self.find(x)==self.find(y)
 
    def link(self,x,y):
        if self.rank[x]<self.rank[y]:
            self.P[x]=y
        elif self.rank[y]<self.rank[x]:
            self.P[y]=x
        else:
            self.P[x]=y
            self.rank[y]+=1
 
    def unite(self,x,y):
        self.link(self.find(x),self.find(y))
 
    def size(self):
        S=set()
        for a in range(self.n):
            S.add(self.find(a))
        return len(S)
def bin_(num,size):
    A=[0]*size
    for a in range(size):
        if (num>>(size-a-1))&1==1:
            A[a]=1
        else:
            A[a]=0
    return A
def comb(n,r):return math.factorial(n)//math.factorial(n-r)//math.factorial(r)
def next_comb(num,size):
    x=num&(-num)
    y=num+x
    z=num&(~y)
    z//=x
    z=z>>1
    num=(y|z)
    if(num>=(1<<size)):return False
    else:
        return num
 

 
#main
L=input()
dp=[[0,0] for _ in range(len(L)+5)]
dp[0][0]=1

ans=0
for a in range(len(L)-1):
    c=L[a]
    #a+b=0
    if c=="0":
        dp[a+1][0]=dp[a][0]
        dp[a+1][1]=dp[a][1]
    else:
        dp[a+1][1]=dp[a][1]+dp[a][0]
    #a+b=1
    if c=="0":
        dp[a+1][1]+=dp[a][1]*2
    else:
        dp[a+1][0]+=dp[a][0]*2
        dp[a+1][1]+=dp[a][1]*2
    dp[a+1][0]%=mod
    dp[a+1][1]%=mod
print((dp[len(L)-1][0]+dp[len(L)-1][1])%mod)