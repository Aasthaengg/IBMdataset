r,d,x  = map(int,input().split())
t = 2000
while t <= 2009:
  x = r*x-d
  print(x)
  t += 1