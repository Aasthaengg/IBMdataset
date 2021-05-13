x = input().split()
a = int(x[0])
b = int(x[1])
if (b % a) == 0:
  print(a+b)
else:
  print(b - a)