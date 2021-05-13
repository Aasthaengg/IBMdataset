dir = int(input())
x = 360
ans = 0

while x != 0:
  if x < 360:
    x += 360
  ans = ans + (x // dir)
  x = x % dir

print(ans)