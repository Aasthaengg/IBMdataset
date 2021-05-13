from collections import *
from itertools import *
import copy
from heapq import *


N,M,R=map(int,input().split())
Rlst=list(map(int,input().split()))
ABC=[list(map(int,input().split())) for i in range(M)]

data=[[100000*200+1 for i in range(N)] for i in range(N)]
for a,b,c in ABC:
    data[a-1][b-1]=c
    data[b-1][a-1]=c

for k in range(N):
    for i in range(N):
        for j in range(N):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])



value=[]
for lst in permutations([i for i in range(R)],R):
    nagasa=0
    for i in range(R-1):
        nagasa+=data[Rlst[lst[i]]-1][Rlst[lst[i+1]]-1]
    value.append(nagasa)
print(min(value))
