MOD = 10**9 + 7
N, K = map(int, input().split())
cusum = [0]
for i in range(1, N+1):
    cusum += [cusum[-1] + i]
ans = 0
for k in range(K, N+1):
    ans += (cusum[N]-cusum[N-k]-cusum[k-1] + 1)
    ans %= MOD
print((ans+1)%MOD)