k = int(input())

a = (k + 1) // 2

if k % 2 == 0:
  print((k // 2) ** 2)
else:
  print(a ** 2 - a)