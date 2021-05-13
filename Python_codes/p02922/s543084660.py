a, b = map(int, input().split())
if b == 1:
  print(0)
  quit()
ans = (b - 1) // (a - 1)
if (b - 1) % (a - 1) != 0:
  ans += 1
print(ans)