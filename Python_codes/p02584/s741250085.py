x, k, d = map(int, input().split())
ans = 0
if abs(x) <= k * d:
  if (abs(x) // d) % 2 == k % 2:
    ans = abs(x) % d
  else:
    ans = d - abs(x) % d
else:
  ans = abs(x) - k * d
print(ans)