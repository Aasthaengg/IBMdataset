from fractions import gcd
n=int(input())
a=list(map(int,input().split()))
b=1
for i in a:
  b=b//gcd(b,i)*i
ans=0
for i in a:
  ans+=(b//i)
print(ans%(10**9+7))