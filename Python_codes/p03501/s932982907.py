x = input().split()
n = int(x[0])
a = int(x[1])
b = int(x[2])
if n*a >= b:
  print(b)
else:
  print(n*a)
