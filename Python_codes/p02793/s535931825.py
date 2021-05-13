from fractions import gcd
MOD=10**9+7
N,*A=map(int,open(0).read().split())

def lcm(a,b):
  return a*b//gcd(a,b)
s=1
for i in A:
  s=lcm(s,i)
s%=MOD
ans=0
for i in A:
  ans+=s*pow(i,MOD-2,MOD)
  ans%=MOD
print(ans)