r,D,x2000 = map(int,input().split())
a = x2000
b = 0
for i in range(10):
  b = r*a - D
  print(b)
  a = b