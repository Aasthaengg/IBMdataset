N, K = map(int, input().split())
res = "NO"
if (N + 1) / 2 >= K:
  res = "YES"
print(res)