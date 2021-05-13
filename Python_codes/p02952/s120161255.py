n=int(input())
ans=0
import math
for i in range(1,n+1):
  if (int(math.log10(i)))%2==0:
    ans=ans+1
print(ans)