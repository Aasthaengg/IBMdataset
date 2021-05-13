X,Y=map(int,input().split())

if X%Y==0:
  print(-1)
else:
  for i in range(1,(10**18)//X+1):
    if i*X%Y!=0:
      print(i*X)
      break