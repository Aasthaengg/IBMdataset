n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 10 ** 9
for l in range(0, n - k + 1):
  r = l + k - 1
  a = abs(x[r]) + abs(x[r] - x[l])
  b = abs(x[l]) + abs(x[r] - x[l])
  ans = min(ans, min(a, b))

print(ans)
