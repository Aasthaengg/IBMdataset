d,n=map(int,input().split())
if n == 100:
  n = 101
if d == 0:
  print(n)
elif d == 1:
  print(str(n) + '00')
else:
  print(str(n) + '0000')