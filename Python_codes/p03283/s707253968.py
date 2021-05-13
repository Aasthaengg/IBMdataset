import sys
import numpy as np

input=sys.stdin.readline

N,M,Q=map(int,input().split())

x=np.zeros((N+1,N+1),dtype=np.int32)
for _ in range(M):
    l,r=map(int,input().split())
    x[l,r]+=1

x=np.cumsum(x,axis=0)
x=np.cumsum(x,axis=1)
for _ in range(Q):
    p,q=map(int,input().split())
    print(x[N,q]-x[p-1,q])