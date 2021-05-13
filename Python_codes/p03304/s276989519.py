n,m,d = map(int,input().split())

if d != 0:
  print((((n-d)*2)/(n**2))*(m-1))
else:
  print(((n-d)/(n**2))*(m-1))
