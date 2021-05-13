from decimal import *
n,k=map(int,input().split())
a=list(map(int,input().split()))
aa=[[0,0] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i>j:
            if a[i]>a[j]:
                aa[i][0]+=1
        if i<j:
            if a[i]>a[j]:
                aa[i][1]+=1
ans=0
mod=10**9+7
for i in range(n):
    ans+=(aa[i][0]+aa[i][1])*k*(k+1)//2
    ans-=aa[i][0]*k
print(int(ans%mod))