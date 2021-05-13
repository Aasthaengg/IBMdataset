# -*- coding: utf-8 -*-
#D - Cake 123
import sys 
from heapq import *
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
X, Y, Z, K = map(int, readline().split())
A = list(map(int,readline().split()))
B = list(map(int,readline().split()))
C = list(map(int,readline().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

q = [(-A[0]-B[0]-C[0],0,0,0)]
heapify(q)
result = []
used = set()

while True:
    S,i,j,k = heappop(q)
    result.append(-S)
    if len(result) == K:
        break
    if i < X-1 and (i+1,j,k) not in used:
        heappush(q,(-A[i+1]-B[j]-C[k],i+1,j,k))
        used.add((i+1,j,k))
    if j < Y-1 and (i,j+1,k) not in used:
        heappush(q,(-A[i]-B[j+1]-C[k],i,j+1,k))
        used.add((i,j+1,k))
    if k < Z-1 and (i,j,k+1) not in used:
        heappush(q,(-A[i]-B[j]-C[k+1],i,j,k+1))
        used.add((i,j,k+1))

print(*result,sep='\n')       