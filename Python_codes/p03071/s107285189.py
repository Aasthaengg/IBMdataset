a,b = map(int,input().split())

x = max(a,b)
y = min(a,b)

if x - 2 >= y:
  print(x + x - 1)
else:
  print(x + y)