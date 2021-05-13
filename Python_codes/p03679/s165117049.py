x,a,b = map(int, input().split())
if a+x < b:
  print("dangerous")
elif a < b:
  print("safe")
else:
  print("delicious")