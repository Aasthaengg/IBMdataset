x, y = map(int, input().split())
ans = 0
if x % y == 0:
  ans = -1
else:
  for i in range(1, (10 ** 18 + 1) // x):
    if x * i % y != 0:
      ans = x * i
      break
  if ans == 0:
    ans = -1
print(ans)