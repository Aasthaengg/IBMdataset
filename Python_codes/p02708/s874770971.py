n, k = map(int, input().split())
mod = 10**9+7
if n - k == -1:
  print(1)
else:
  ans = (n+2*k) * (n-k+1) * (n-k+2) // 6 + n - k + 2
  print(ans%mod)
