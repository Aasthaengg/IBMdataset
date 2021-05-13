n, k = map(int, input().split())

l = []
r = []
for i in range(k):
  a, b = map(int, input().split())
  l.append(a)
  r.append(b)

mod = 998244353

dp = [0] * (n + 1)
#１マス目の行き方は１通り
dp[1] = 1
dpsum = [0] * (n + 1)
dpsum[1] = 1
for i in range(2, n + 1):
  for j in range(k):
    li = i - r[j]
    ri = i - l[j]
    if ri < 0:
      continue
    li = max(1, li)

    dp[i] += (dpsum[ri] - dpsum[li - 1]) % mod
  
  dpsum[i] = dpsum[i - 1] + dp[i]

print(dp[n] % mod)

