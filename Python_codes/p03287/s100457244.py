# coding: utf-8
# Your code here!
N,M=map(int,input().split())
A=list(map(int,input().split()))

ans=0
wa=0
log={0:1}
for i in range(len(A)):
    wa+=A[i]
    if wa%M in log:
        ans+=log[wa%M]
        log[wa%M]+=1
    else:
        log[wa%M]=1
print(ans)

