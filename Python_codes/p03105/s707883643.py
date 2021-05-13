a, b, c = map(int, input().split())
 
if a <= b:
  x = b // a
  if x >= c:
    print(c)
  else:
    print(x)
else:
  print(0)