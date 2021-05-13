a, b, c = map(int, input().split())

if (c <= a - b):
  print(0)
  exit()
print(c - (a - b))