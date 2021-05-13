a, b = map(int, input().split())
ans = 0

for i in range(1270):
  x = i * 8
  y = x / 100
  z = i * 10
  q = z / 100
  if a == int(y) and b == int(q):
    if ans == 0:
      ans = i
    else:
      ans = min(ans, i)

if ans == 0:
  print(-1)
else:
  print(ans)