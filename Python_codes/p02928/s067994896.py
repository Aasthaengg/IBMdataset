MOD = 10**9 + 7

N, K = map(int, input().split())
A = tuple(map(int, input().split()))

ans = 0

for i, a in enumerate(A):
  before = 0
  after = 0
  for j, b in enumerate(A):
    if a > b:
      if i < j:
        after += 1
      else:
        before += 1
    
  ans += (after * K * (K + 1) // 2) % MOD
  ans += (before * K * (K - 1) // 2) % MOD
  ans %= MOD

print(ans)
