n, k = map(int, input().split())
a = [i for i in range(n+1)]
mod = 10**9+7
ans = 0
for i in range(k, n+2):
  L = i * (i - 1) / 2
  R = n * i - i * (i - 1) / 2
  ans += R - L + 1
  ans %= mod
print(int(ans))