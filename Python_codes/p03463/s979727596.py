N,A,B=map(int,input().split())
count=1
while B-A!=1:
  if count%2==1:
    A+=1
  else:
    B-=1
  count+=1
if count%2==1:
  print('Borys')
else:
  print('Alice')