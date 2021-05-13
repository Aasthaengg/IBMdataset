from fractions import gcd
def lcm(a,b):
  return a*b//gcd(a,b)
n=int(input())
a=list(map(int,input().split()))
ans=0
mod=10**9+7
l=a[0]
for i in range(1,n):
  l=lcm(l,a[i])
l%=mod
for aa in a:
  #　mod(10**9+7)逆元
  ans+=l*pow(aa,mod-2,mod)%mod
  ans%=mod
print(ans)