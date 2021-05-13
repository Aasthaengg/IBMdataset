def main():
    N,K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    MOD = 10**9+7

    fact = [1] * (N+1) # 階乗を格納するリスト
    factinv = [1] * (N+1) # 階乗を格納するリスト
    # 毎回mod演算を行って計算量を削減しているのもポイント
    for i in range(N):
        fact[i+1] = fact[i] * (i+1) % MOD # 階乗を計算
        factinv[i+1] = pow(fact[i+1], MOD-2, MOD) # MODを法とした逆元（フェルマーの小定理）
    def comb(n,k): # 組み合わせ(MOD)を返却する
        return fact[n] * factinv[n-k] * factinv[k] % MOD

    ans = 0
    # minX全てを計算
    for i in range(N-K+1):
        ans -= A[i]*comb(N-i-1,K-1)
        ans %= MOD

    A = A[::-1]
    # maxX全てを計算
    for i in range(N-K+1):
        ans += A[i]*comb(N-i-1,K-1)
        ans %= MOD

    print(ans)
main()
