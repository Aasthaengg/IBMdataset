n, k = map(int, input().split())
if n == 1:
  print(k)
else:
  ans = k
  for _ in range(2, n + 1):
    ans *= (k - 1)
  print(ans)