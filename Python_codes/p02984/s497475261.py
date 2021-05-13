#!/usr/bin/ python3.8
N=int(input())
A=[int(x) for x in input().split()]
a=[0]*N
for i in range(N):
    if i%2==0:
        a[0]+=A[i]
    else:
        a[0]-=A[i]
assert a[0]>=0 and a[0]%2==0
A[0]-=a[0]//2
A[N-1]-=a[0]//2
for i in range(0,N-1):
    a[i+1]=2*A[i]
    A[i]-=a[i+1]//2
    A[i+1]-=a[i+1]//2
print(*a)
