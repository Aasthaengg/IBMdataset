x,n = map(int,input().split())

if n == 0:
  print(x)
else:
  p = set(map(int,input().split()))
  i = 0
  while True:
    x_p,x_n = x+i,x-i
    if not x_n in p:
      print(x_n)
      break
    if not x_p in p:
      print(x_p)
      break
    i += 1