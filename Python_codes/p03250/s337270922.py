a,b,c = map(int, input().split())
if max(a,b,c) == a:
  print(10*a+b+c)
elif max(a,b,c) == b:
  print(10*b+a+c)
else:
  print(10*c+a+b)
