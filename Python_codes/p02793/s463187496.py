from math import gcd
mod=10**9+7
n=int(input())
a=list(map(int,input().split()))
c=a[0]
for i in a[1:]:
  c=c*i//gcd(c,i)
ans=0
c%=mod
for i in a:
  ans+=c*pow(i,mod-2,mod)
  ans%=mod
print(ans)