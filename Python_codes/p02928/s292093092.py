MOD = int(1e9) + 7
N,K = map(int,input().split())
A = list(map(int, input().split()))
ans = 0
inv = pow(2,MOD-2,MOD)
for i in range(N):
    cnt = 0
    for j in range(N):
        if A[i] > A[j]:
            cnt += 1
    ans += (cnt * K * (K-1) * inv) % MOD
    for j in range(i,N):
        if A[i] > A[j]:
            ans += K
            ans %= MOD
    ans %= MOD
print(ans)
