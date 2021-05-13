import sys
d,n = map(int,input().split())
num = 100**d
if n == 100:
  print(101*num)
  sys.exit()
if d == 0:
  print(n)
else:
  print((100**d)*n)