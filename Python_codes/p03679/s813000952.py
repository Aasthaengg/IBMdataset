x,a,b=map(int, input().split())
date=b-a
if date<=0:
  print("delicious")
elif date<=x:
  print("safe")
else:
  print("dangerous")
