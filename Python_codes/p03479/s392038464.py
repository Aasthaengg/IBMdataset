x, y = map(int, input().split())

for i in range(1, 10000):
  x *= 2
  if x > y:
    print(i)
    break