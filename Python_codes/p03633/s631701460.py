import math

n=int(input())
ans=int(input())

if n>1:
  
  for x in range(n-1):
    s=int(input())
    ans=ans*s//(math.gcd(ans,s))
    
  
print(ans)