a, b = [int(i) for i in input().split()]
tmp = a + b
if tmp >= 24:
  print(tmp % 24)
else:
  print(tmp)