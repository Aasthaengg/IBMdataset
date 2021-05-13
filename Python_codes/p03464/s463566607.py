n=int(input())
a=list(map(int,input().split()))[::-1]
if a[0]!=2:
  print(-1)
  exit()
mn,mx=2,2
for j in a:
  if (mn+j-1)//j>mx//j:
    print(-1)
    exit()
  mn=(mn+j-1)//j*j
  mx=mx//j*j+j-1
print(mn,mx)