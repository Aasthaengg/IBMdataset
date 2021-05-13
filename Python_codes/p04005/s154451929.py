a, b, c = (int(x) for x in input().split())
if (a*b*c)%2 == 0:
  print(0)
else:
  print(min(a*b, b*c, c*a))