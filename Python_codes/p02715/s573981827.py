def solve():
    N, K = map(int,input().split())
    mod = 10 ** 9 + 7

    cnt = [0] * (K+1)
    for g in range(K,0,-1):
        cnt[g] = pow(K // g, N, mod)
        gg = g * 2
        while gg <= K:
            cnt[g] -= cnt[gg]
            gg += g
    
    ans = 0
    for i in range(1,K+1):
        ans += cnt[i] * i % mod
    print(ans%mod)

if __name__ == '__main__':
    solve()
