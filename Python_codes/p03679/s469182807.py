x,a,b = list(map(int,input().strip().split()))

if a-b >= 0:
  print("delicious")
elif a-b >= -1*x:
  print("safe")
else:
  print("dangerous")