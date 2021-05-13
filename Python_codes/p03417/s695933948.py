n,m = map(int,input().split())
if n == 2 or m == 2:
  print(0)
elif n == 1:
  if m == 1:
    print(1)
  else:
    print(m-2)
elif m == 1:
  if n == 1:
    print(1)
  else:
    print(n-2)
else:
  print((n-2)*(m-2))