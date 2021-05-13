# coding: utf-8
# Your code here!
import math
N=int(input())
A=list(map(int,input().split()))
cnt=0
ans=0
for i in range(N-1):
    #print(cnt)
    if A[i]==A[i+1]:
        cnt+=1
    else:
        ans+=(math.ceil(cnt/2))
        cnt=0
ans+=math.ceil(cnt/2)
print(ans)