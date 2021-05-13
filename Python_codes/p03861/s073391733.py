a, b, x = map(int, input().split())
c = b // x + 1
d = 0
if a - 1 > -1:
  d = (a - 1) // x + 1
else:
  d = 0
print(c - d)