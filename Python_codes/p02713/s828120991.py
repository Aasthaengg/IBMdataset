from math import gcd
from functools import reduce
n=int(input())
ans=0
for i in range(1,n+1):
  for j in range(i+1,n+1):
    for k in range(j+1,n+1):
      ans+=reduce(gcd,(i,j,k))*6
for i in range(1,n+1):
  for j in range(i+1,n+1):
    ans+=gcd(i,j)*6
for i in range(n+1):
  ans+=i
print(ans)