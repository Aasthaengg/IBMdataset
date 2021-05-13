A, B = map(int, input().split())
if B == 1:
  print(0)
  exit()
x = 1
while x * (A - 1) < B - 1:
  x += 1
print(x)