a, b, c = map(int, input().split())
ans = 0
if a == b == c and a != 1:
  ans = -1
else:
  while a % 2 == b % 2 == c % 2 == 0:
    x = a // 2
    y = b // 2
    z = c // 2
    if x % 2 == y % 2 == z % 2:
      a = y + z
      b = z + x
      c = z + x
      ans += 1
    else:
      ans += 1
      break
print(ans)