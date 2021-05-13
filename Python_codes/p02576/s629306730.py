n, x, t = [int(x) for x in input().split()]

a, b = divmod(n, x)

if b:
  print((a+1) * t)
else:
  print(a * t)