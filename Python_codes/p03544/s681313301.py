n = int(input())
x = 2
y = 1

for i in range(n):
  if i % 2 == 0:
    x = x + y
  else:
    y = x + y

if n % 2 == 0:
  print(x)
else:
  print(y)