import sys
l,r = map(int,input().split())
if l+2019<=r:
  print(0)
  sys.exit()
l=l%2019
r=r%2019
if l>=r:
  print(0)
  sys.exit()

ans=2018
for i in range(l,r):
  if ans == 0:
    break
  for j in range(i+1,r+1):
    ans = min(ans,i*j%2019)
    if ans == 0:
      break
print(ans)