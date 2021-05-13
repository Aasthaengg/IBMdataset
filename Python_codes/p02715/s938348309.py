n,k = map(int,input().split())
mod = 10**9+7
L = [0 for i in range(k+1)]
for i in range(k, 0, -1):
    t = pow(k//i, n, mod)
    cnt = 2
    while cnt*i <= k:
        t -= L[cnt*i]
        cnt += 1
    L[i] = t
ans = 0
for i in range(1,k+1):
    ans += i*(L[i]%mod)%mod
    ans %= mod
print(ans%mod)