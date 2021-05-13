N=int(input())
M=list(map(int, input().split()))
ans=min(M)
mn=min(M)
from math import gcd
for m in M:
  if m%mn!=0:
    ans=min(ans, gcd(mn,m))
print(ans)
