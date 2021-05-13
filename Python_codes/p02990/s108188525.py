N, K = map(int, input().split())
mod = 10 ** 9 + 7
for i in range(1, K+1):
    if i > N - K + 1:
        print(0)
    else:
        ans = 1
        tmp = 1
        for j in range(K - i):
            ans = ans * (K - 1 - j )% mod
            tmp = tmp * (K - i - j) % mod
        for k in range(N - K - i + 1):
            ans = ans * (N - K + 1 - k) % mod
            tmp = tmp * (N - K - i + 1 - k) % mod
        ans = ans % mod * pow(tmp, mod - 2, mod) % mod
        print(ans)