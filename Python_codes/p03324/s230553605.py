d,n = map(int,input().split())
if n == 100:
  print(101*(100**d))
  exit()
  
if d == 0:
  print(n)
elif d == 1:
  print(100*n)
else:
  print(10000*n)
