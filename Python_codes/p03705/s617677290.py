from itertools import product

n, a, b = map(int, input().split())

if a > b :
  print(0)
  exit()
elif n == 1:
  if a != b:
    print(0)
    exit()
  else:
    print(1)
    exit()
else:
  print((b-a) * (n-2) + 1)