n = int(input())
if n%2 == 1:
  print(0)
else:
  i = 0
  a = n//10
  b = 1
  while b != 0:
    i += 1
    b = n//((5**i)*10)
    a += b
  print(a)