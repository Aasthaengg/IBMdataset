X = int(input())
for k in range(1, 361):
  if k * X % 360 == 0:
    print(k)
    break