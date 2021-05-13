l,r=map(int,input().split())

if r-l>2019:
  print(0)
else:
  mn=2019
  for i in range(l,r):
    for j in range(i+1,r+1):
      mn=min(mn,(i*j)%2019)
  print(mn)