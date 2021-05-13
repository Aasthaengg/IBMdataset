x,a,b = map(int, input().split())

if b-a > x:
  print("dangerous")
else:
  print("delicious" if a>=b else "safe")
