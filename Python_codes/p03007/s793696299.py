# coding: utf-8
N=int(input())
A=list(map(int,input().split()))

A.sort()

MIN=A[0]
MAX=A[-1]

if MIN>0:
    print(sum(A)-MIN*2)
elif MAX<0:
    print(-(sum(A)-MAX*2))
else:
    M=0
    for i in range(N):
        M+=abs(A[i])
    print(M)
    

for i in range(1,N-1):
    if A[i]<0:
        print(MAX,A[i])
        MAX-=A[i]
    else:
        print(MIN,A[i])
        MIN-=A[i]

print(MAX,MIN)