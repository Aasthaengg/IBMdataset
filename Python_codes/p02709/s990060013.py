def solve(n, aaa):
    dp = [0]
    aaa_with_idx = list(zip(aaa, range(n)))
    aaa_with_idx.sort(reverse=True)
    for k in range(1, n + 1):
        ndp = [0] * (k + 1)
        a, i = aaa_with_idx[k - 1]
        for l in range(k):
            # 左に配置
            ndp[l + 1] = max(ndp[l + 1], dp[l] + a * abs(i - l))
            # 右に配置
            r = n - (k - l)
            ndp[l] = max(ndp[l], dp[l] + a * abs(i - r))
        dp = ndp
    return max(dp)


n = int(input())
aaa = list(map(int, input().split()))
print(solve(n, aaa))
