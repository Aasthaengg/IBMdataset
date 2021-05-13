a,b,c,d = map(lambda x: int(x), input().split())

if a*b <= c*d:
  print(c*d)
else:
  print(a*b)