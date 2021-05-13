#coding:utf-8
N=input()
A=map(int,raw_input().split())
ans=0
s=0
r=0
for l in range(N):
    while (r<N and s+A[r]==s^A[r]):
        s+=A[r]
        r+=1
    ans+=r-l
    if l==r:r+=1
    else: s-=A[l]
print(ans)    


