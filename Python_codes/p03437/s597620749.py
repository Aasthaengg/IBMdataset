x, y = map(int, input().split())
if x == y or x % y == 0:
  print(-1)
else:
  now = x
  k = 1
  M = pow(10, 18)
  while now <= M:
    now = k * now
    if now % y != 0:
      break
    k += 1
  print(now)