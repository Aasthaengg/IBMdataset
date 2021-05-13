x = int(input())
n = 1
while True:
  if (x * n) % 360 == 0:
    print(n)
    exit(0)
  n += 1