a, b, c = map(int, input().split())
if a == 0:
  print(b // c+1)
  exit()
print(b // c - (a-1) // c)