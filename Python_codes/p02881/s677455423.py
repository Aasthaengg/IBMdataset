n=int(input())
import math
ans=10**12
i=0
while i*i<=n:
  i+=1
  if n%i!=0:
    continue
  j=n/i
  ans=min(ans, i+j-2)
if ans ==10**12:
  print(n-1)
else:
  print(int(ans))
