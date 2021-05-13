N, K = map(int, input().split())  # N個の数列, K以下の数字で構成される
gcd_sum = [0]*(K+1)
MOD = 10**9+7
# 最大公約数がKになる通りが何パターンあるかを求める
for i in reversed(range(1, K+1)):
    # パターン数にMODを取っても問題ない（結局掛け算しかしないので）
    gcd_sum[i] = pow(K//i, N, MOD)
    cur = 2*i
    while cur <= K:
        gcd_sum[i] -= gcd_sum[cur]
        cur += i
ans = 0
for i in range(1, K+1):
    ans += gcd_sum[i]*i
    ans %= MOD
print(ans)
