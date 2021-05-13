# coding: utf-8
n=int(input())
l = list(map(int,input().split()))
heikin=sum(l)/n
tmp=float('inf')
ans=n-1
for i in range(n-1,-1,-1):
    if abs(l[i]-heikin) <= tmp:
        ans=i
        tmp=abs(l[i]-heikin)
print(ans)