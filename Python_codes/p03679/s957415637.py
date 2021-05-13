x,a,b = map(int,input().split())

if x+a-b < 0:
  print("dangerous")
else:
  if a >= b:
    print("delicious")
  else:
    print("safe")
