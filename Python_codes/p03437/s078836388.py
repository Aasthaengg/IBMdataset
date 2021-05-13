x,y=map(int,input().split())
if x%y==0:
  print(-1)
else:
  i=2
  while True:
    if x*i%y!=0:
      print(x*i)
      break
    else:
      i=i+1