r, D, x0 = map(int, input().split())

x_prev = x0
for _ in range(10):
  weight = r * x_prev - D
  print(weight)
  x_prev = weight