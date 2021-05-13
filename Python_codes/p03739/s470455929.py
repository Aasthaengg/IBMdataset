import sys,copy
from itertools import accumulate

input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

A=list(accumulate(A))
B=copy.copy(A)
test1=0
s=0
for i in range(0,N):
    A[i]+=s
    if i%2==0:
        if 0>=A[i]:
            test1+=1-A[i]
            s+=1-A[i]
    else:
        if A[i]>=0:
            test1+=A[i]+1
            s-=A[i]+1


test2=0
s=0
for i in range(0,N):
    B[i]+=s
    if i%2==0:
        if B[i]>=0:
            test2+=B[i]+1
            s-=B[i]+1
    else:
        if 0>=B[i]:
            test2+=1-B[i]
            s+=1-B[i]

print(min(test1,test2))