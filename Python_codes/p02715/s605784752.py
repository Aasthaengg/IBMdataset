N, K = map(int, input().split())
MOD = 10 ** 9 + 7

l = [0 for _ in range(K + 1)]
for i in range(1, K + 1):
  l[i] = pow(K//i, N, MOD)

for i in range(K, 0, -1):
  for j in range(i * 2, K + 1, i):
    l[i] -= l[j]
    l[i] %= MOD

ans = 0
for i in range(1, K + 1):
  ans += l[i] * i % MOD
  ans %= MOD
print(ans)