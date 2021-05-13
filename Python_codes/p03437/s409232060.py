x,y=map(int,input().split())
if x%y==0:
  print("-1")
else:
  for i in range(1,x*y):
    if x*i%y!=0:
      print(x*i)
      exit()