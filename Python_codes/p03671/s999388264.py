a, b, c = map( int, input().split() )

x = max(a,b,c)
if a == x:
  print(b+c)
elif b == x:
  print(a+c)
else:
  print(a+b)