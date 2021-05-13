a, b = (int(x) for x in input().split())
x = (a+b) / 2
if (a+b) % 2 == 0:
  print(int(x))
else:
  print(int(x + 0.5))