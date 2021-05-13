def main():
    MOD = 998244353
    n, k = map(int, input().split())
    L, R = [], []
    for _ in range(k):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (n + 1)
    s = [0] * (n + 1)
    dp[1] = 1
    s[1] = 1
    for i in range(2, n + 1):
        for j in range(k):
            l = max(1, i - R[j])
            r = i - L[j]
            if r < 1: continue
            dp[i] += s[r] - s[l - 1]
            dp[i] %= MOD
        s[i] = s[i - 1] + dp[i]
        s[i] %= MOD
    print(dp[n])


if __name__ == "__main__":
    main()
