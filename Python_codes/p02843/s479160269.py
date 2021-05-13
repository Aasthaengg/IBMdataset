x = int(input())
if x >= 2000:
  print(1)
else:
  n = x // 100
  d = x % 100
  if n * 5 >= d:
    print(1)
  else:
    print(0)