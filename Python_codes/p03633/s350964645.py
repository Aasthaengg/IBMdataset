from math import gcd
N=int(input())
ans=int(input())
for i in range(N-1):
  t=int(input())
  ans=ans*t//gcd(ans, t)
  
print(ans)
