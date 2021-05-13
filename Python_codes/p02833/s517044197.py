n = int(input())
if n % 2 == 1:
  print(0)
else:
  a = 0
  m = n // 2
  while True:
    m = m // 5
    a += m
    if m == 0:
      break
  print(a)
