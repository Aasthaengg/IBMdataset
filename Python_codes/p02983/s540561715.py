import sys
l,r=map(int,input().split())

if (r-l) > 2100:
  print(0)
  sys.exit()

ans=9999

for i in range(l,r):
  for j in range(i+1,r+1):
    ans=min(ans,(i*j)%2019)
print(ans)