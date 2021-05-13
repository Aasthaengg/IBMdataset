h, n = map(int, input().split())

ab = []
for i in range(n):
  a,b = map(int, input().split())
  ab.append([a, b])


dp = [10**9 for i in range((h+1)+10000)]
dp[0] = 0
for i in range(1, (h+1)+10000):
  for j in range(n):
    a, b = ab[j]
    if a > i:
      continue
    dp[i] = min(dp[i], dp[i-a]+b)

x = min(dp[h:])
print (x)