n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
ans=0
d=1
for i in range(61):
  s=0
  for j in a:
    s+=(j>>i)&1
  ans+=s*(n-s)*d%mod
  ans%=mod
  d*=2
  d%=mod
print(ans)