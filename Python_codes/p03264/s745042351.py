k = int(input())

r = k % 2
x = k // 2
y = (k + 1) // 2
z = (k - 1) // 2

if r == 0:
  print(x ** 2)
else:
  print(y * z)