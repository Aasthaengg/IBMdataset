#from collections import *
#from itertools import *
#from bisect import *
from heapq import *
#import copy
#N=int(input())
#X,Y=map(int,input().split())
#S=list(map(int,input().split()))
#S=[list(map(int,input().split())) for i in range(N)]

N,M=map(int,input().split())
A=sorted(list(map(int,input().split())),reverse=True)
"""
lst=[]
for i in range(N):
    for m in range(N):
        lst.append(A[i]+A[m])
lst=sorted(lst,reverse=True)
#print(sum(lst[:M]))
print(lst)
"""
ng=-1
ok=max(A)*2+1
while ok>ng+1:
    mid=(ok+ng)//2
    K=0
    idx=0
    for i in range(N-1,-1,-1):
        X=mid-A[i]
        while idx<N and A[idx]>=X:
            idx+=1
        K+=idx
    if K>M:
        ng=mid
    else:
        ok=mid
idx=0
lst=[0 for i in range(N)]
for i in range(N-1,-1,-1):
    X=ng-A[i]
    while idx<N and A[idx]>=X:
        idx+=1
    lst[i]=idx*2
value=0
for a,i in zip(A,lst):
    value+=a*i
value-=ng*(sum(lst)//2-M)
print(value)
