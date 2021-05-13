X = int(input())

count = 1
while True:
  if 100*count <= X <= 105*count:
    print(1)
    exit()
  elif X < 100*count:
    print(0)
    exit()
  count += 1