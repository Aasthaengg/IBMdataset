# input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
# import functools
# import itertools
# import math

N,M=map(int,input().split())
A=list(map(int,input().split()))
#A=[i%M for i in A]
data=[0 for i in range(N)]
data[0]=A[0]%M
for i in range(1,N):
    data[i]=(data[i-1]+A[i])%M
data.append(0)
data=Counter(data)
print(sum([data[i]*(data[i]-1)//2 for i in data if data[i]>=2]))
