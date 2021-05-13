# coding: utf-8
# Your code here!
N=int(input())
A=list(map(int,input().split()))
A.sort()

log=[0]*10**6
ans=len(A)

for a in A:
    if log[a-1]==0:
        log[a-1]=-1
        for index in range(a-1+a,10**6,a):
            log[index]=1
    elif log[a-1]==-1:
        log[a-1]=1
        ans-=2
    else:
        ans-=1

print(ans)