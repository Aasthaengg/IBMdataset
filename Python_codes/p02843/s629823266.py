X = int(input())
for i in range(1, 10**10):
  if 100*i <= X <= 105*i:
    print(1)
    break
  elif X < 100*i:
    print(0)
    break