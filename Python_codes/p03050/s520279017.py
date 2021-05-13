from math import *
n=int(input())
nn=sqrt(n)
ans=0
for k in range(1,int(nn)+1):
    if n%k==0:
        m=-1+n//k
        if m>k:
            ans+=m
print(ans)