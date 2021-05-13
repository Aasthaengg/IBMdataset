a,b = map(int,input().split())
if a==b:
  print(2*b)
else:
  x = max(a,b)
  print(2*x-1)
