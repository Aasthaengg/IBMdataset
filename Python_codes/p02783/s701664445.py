#153a
h, a = map(int, input().split())

for i in range(10 ** 4):
  h -= a
  if h <= 0:
    print(i + 1)
    break