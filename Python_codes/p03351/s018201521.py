a, b, c, d = map(int, input().split())
ans = max(abs(a - b), abs(b - c))
ans = min(ans, abs(a - c))

if ans > d:
  print("No")
else:
  print("Yes")