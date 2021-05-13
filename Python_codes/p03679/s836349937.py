a,b,c = list(map(int,input().split()))
if b >= c:
  print("delicious")
elif a+b < c:
  print("dangerous")
else:
  print("safe")