def p_e():
    n, t = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ma = ab[-1][0]
    dp = [0] * (t + ma)
    for w, v in ab:
        next = [0] * (t + ma)
        for j in range(1, t + ma):
            if 0 <= j - w < t:
                next[j] = max(dp[j - w] + v, dp[j])
            else:
                next[j] = dp[j]
        dp = next
    print(max(dp))
    
p_e()