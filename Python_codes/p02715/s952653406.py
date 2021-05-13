N, K = map(int, input().split())
MOD = 10**9+7
cnt = [0]*(K+1)
ans = 0

for i in range(K, 1, -1):
    cnt[i] = pow(K//i, N, MOD)
    
    for j in range(2*i, K+1, i):
        cnt[i] -= cnt[j]
        cnt[i] %= MOD
    
    ans += i*cnt[i]

ans += pow(K, N, MOD)-sum(cnt[2:])
ans %= MOD

print(ans)