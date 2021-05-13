k, a, b = map(int, input().split())

ans = 0
if b - a < 2:
  ans = k + 1
else:
  ans = a
  k -= a - 1
  ans += (b - a) * (k // 2) + k % 2

print(ans)
