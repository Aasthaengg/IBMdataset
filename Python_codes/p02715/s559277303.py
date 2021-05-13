def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    cnt = [0 for _ in range(K)] # k番目の要素はgcd(A)==k+1(x)となるような数列Aの個数
    ans = 0

    for k in range(K)[::-1]:
        x = k+1

        ### gcd(A)がxの倍数となるような数列Aの個数
        cnt[k] = pow((K//x), N, MOD) # (K//x)**Nでは計算量がかかる
        cnt[k] %= MOD
        ### gcd(A)が2x, 3x...となる数列Aの個数を引く。
        for j in range(2*x, K+1, x):
            cnt[k] -= cnt[j-1]
            cnt[k] %= MOD

        ans += cnt[k]*x
        ans %= MOD
    print(ans)
main()