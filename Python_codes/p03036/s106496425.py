r, D, x2000 = map(int, input().split())

x_add = x2000
for i in range(10):
  x_print = r * x_add - D
  print(x_print)
  x_add = x_print