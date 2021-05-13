N, K = map(int, input().split())
mod = 10**9+7

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range(2, 2001):
    g1.append((g1[-1]*i)%mod)
    
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)

def func(N, K, mod):
    if K<0 or K>N:
        return 0
    K = min(K, N-K)
    return g1[N] * g2[K] * g2[N-K] % mod

for i in range(1, K+1):
    ans = func(N-K+1, i, mod)*func(K-1, i-1, mod)%mod
    print(ans)