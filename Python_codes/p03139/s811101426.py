n, a, b = map(int, input().split())
ans1 = min(a, b)
if a + b < n:
  ans2 = 0
else:
  ans2 = abs(n - a - b)
print(ans1, ans2)