k, a, b = map(int, input().split())
ans = k + 1
if a <= k:
  ans2 = a
  k -= a - 1
  if k % 2 == 1:
    ans2 += 1
  ans2 += (b - a) * (k // 2)
print(max(ans, ans2))