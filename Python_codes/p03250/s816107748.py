a, b, c = map(int, input().split())

x = 10*a+b+c
y = 10*b+c+a
z = 10*c+a+b

if x>y and x>z:
  print(x)
elif y > z:
  print(y)
else:
  print(z)