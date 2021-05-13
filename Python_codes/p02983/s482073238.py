l,r=map(int,input().split())
import sys
mod=2019
ans=float('inf')

for i in range(l,r+1):
  for j in range(i+1,r+1):
    ans=min((i*j)%mod,ans)
    if ans==0:
      print(0)
      sys.exit()
print(ans)