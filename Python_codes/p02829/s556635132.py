x,y=map(int,open(0).read().split())
for i in range(1,4):
  if x==i or y==i:
    continue
  print(i)