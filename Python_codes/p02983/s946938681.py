import sys
l,r=map(int,input().split())
if l+2019<=r:
  print(0)
  sys.exit()
mn=2018*2018
for i in range(l,r+1):
  for j in range(i+1,r+1):
    mn=min(mn,i*j%2019)
print(mn)