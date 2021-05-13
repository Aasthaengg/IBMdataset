MOD = 10**9+7
N, K = map(int, input().split())  # N個の整数列, 要素は1~Kの値を取る
# 数列の最大公約数がk(1<=k<=K)の通りを考える
ans = 0
cnt = [0]*(K+1)
for k in reversed(range(1, K+1)):
    cnt[k] = pow((K//k), N, MOD)
    tmp = k * 2  # 2倍したもの
    while tmp <= K:
        cnt[k] -= cnt[tmp]
        tmp += k
for i in range(K+1):
    ans += cnt[i]*i
    ans %= MOD
print(ans)
