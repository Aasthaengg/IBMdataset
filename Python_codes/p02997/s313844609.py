from collections import *
from itertools import *
import copy
from heapq import *


N,K=map(int,input().split())
if K>(N-1)*(N-2)//2:
    print(-1)
    exit()

count=(N-1)*(N-2)//2-K
relst=[]
lst=[i for i in range(1,N)]
for l in lst:
    relst.append([l,N])


for l1 in range(1,N):
    for l2 in range(l1+1,N):
        if count>0:
            relst.append([l1,l2])
            count-=1
        else:
            break
print(len(relst))
for a,b in relst:
    print(a,b)
