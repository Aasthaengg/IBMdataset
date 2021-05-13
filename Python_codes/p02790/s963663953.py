a, b = input().split()

x = a
y = b

if int(a) >= int(b):
  for i in range(int(a)-1):
    y += b
  print(int(y))

else:
  for i in range(int(b)-1):
    x += a
  print(int(x))