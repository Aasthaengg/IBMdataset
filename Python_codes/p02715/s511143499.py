from functools import reduce

MOD = 10**9 + 7
N, K = map(int, input().split())
cnt = [0] * (K + 1)
ans = 0
for k in range(K, 0, -1):
    temp = cnt[2*k::k]
    cnt[k] = pow(K // k, N, MOD) - (reduce(lambda x, y: (x + y) % MOD, temp) if temp else 0)
    ans += (cnt[k] * k) % MOD; ans %= MOD
print(ans)