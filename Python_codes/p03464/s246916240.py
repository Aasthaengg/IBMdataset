# input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
import copy
K=int(input())
A=list(map(int,input().split()))
if A[-1]!=2:
    print(-1)
    exit()

maX=2
miN=2

for i in range(K-1,-1,-1):

    if A[i]//maX>=2:
        print(-1)
        exit()
    if A[i]//miN>=2:
        miN=A[i]
    else:
        if miN%A[i]==0:
            pass
        else:
            miN=(miN//A[i] +1) *A[i]
    maX=maX-maX%A[i] + A[i]-1

mmaX=maX
for i in range(K):
    mmaX-=mmaX%A[i]
if mmaX==2:
    print(miN,maX)
else:
    print(-1)
