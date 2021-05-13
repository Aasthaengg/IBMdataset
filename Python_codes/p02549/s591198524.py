def solve():
    N, K = map(int,input().split())
    L = []
    R = []
    MOD = 998244353
    for _ in range(K):
        l, r = map(int,input().split())
        L.append(l)
        R.append(r)
    
    dp = [0] * (N+1)
    dp[1] = 1
    acc = [0] * (N+1)
    acc[1] = 1

    for i in range(2,N+1):
        for j in range(K):
            if i - L[j] < 0:
                continue
            dp[i] += (acc[i-L[j]] - acc[max(0,i-R[j]-1)]) % MOD
            dp[i] %= MOD
        
        acc[i] = (acc[i-1] + dp[i]) % MOD
    
    print(dp[-1])
if __name__ == '__main__':
    solve()