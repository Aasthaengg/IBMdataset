import collections
n=int(input())
s=input()
c=collections.Counter(s)
mod=10**9+7

ans=1
for i,m in c.items():
    ans*=(m+1)
    ans%=mod
print(ans-1)