n,y=map(int,input().split())
y//=1000
f=False
for yu in range(n+1):
  for hi in range(n+1):
    if y<yu*10+hi*5:
      continue
    if y-(yu*10+hi*5)==n-(yu+hi):
      print(yu,hi,n-yu-hi)
      f=True
      break
  if f:
    break
else:
  print("-1 -1 -1")