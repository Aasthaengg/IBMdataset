N, K = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
GCD = [0 for i in range(K+1)]
for i in range(K, 0, -1):
    # gcd(a1,a2,a3....an)=i の物の数
    S = pow(K//i, N, mod)
    for j in range(2, K//i + 1):
        S -= GCD[j*i]
    GCD[i] = S % mod
for i in range(1, K+1):
    ans += GCD[i]*i
    ans %= mod
print(ans)