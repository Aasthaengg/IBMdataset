# coding: utf-8
N=int(input())
A=list(map(int,input().split()))

A.sort()
ans=max(A)

for i in range(N-2):
    ans+=A[-(2+i//2)]

print(ans)
