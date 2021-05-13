x,a,b=map(int,input().split())
if b-a>0:
  if b-a>x:
    print("dangerous")
  else:
    print("safe")
else:
  print("delicious")