n, a, b = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
for x1, x2 in zip(x, x[1:]):
  ans += min(a * (x2 - x1), b)
print(ans)