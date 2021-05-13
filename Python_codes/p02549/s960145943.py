n, k = map(int, input().split())
mod = 998244353
d = [0] * (n + 1)
d[1] = 1
LR =[list(map(int, input().split())) for _ in range(k)]

for i in range(2, n+1):
  d[i] = d[i - 1]
  for l, r in LR:
    if i - l <= 0:
      continue
    d[i] = (d[i] + (d[i-l] - d[max(0,i-r-1)])) % mod
print((d[-1] - d[-2])%mod)