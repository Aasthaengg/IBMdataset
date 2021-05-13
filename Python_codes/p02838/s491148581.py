n = int(input())
a = list(map(int, input().split()))

ans = 0
mod = 10**9+7
for i in range(60):
  cnt_zero = 0
  cnt_one = 0
  for j in range(n):
    if a[j] >> i & 1:
      cnt_one += 1
    else:
      cnt_zero += 1
  ans += 2**i*cnt_zero*cnt_one
  ans %= mod
print(ans)