# coding: utf-8
# Your code here!
n=int(input())
A=list(map(int,input().split()))
minA=A[0]
ans=0
for i in range(n):
    if A[i]<=minA:
        ans+=1
        minA=min(A[i],minA)
print(ans)