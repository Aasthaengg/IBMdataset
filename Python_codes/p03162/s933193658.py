def edu_dp_c_vacation():
    n = int(input())
    v = []
    for _ in range(n):
        v.append(list(map(int, input().split())))
    dp = [[0]*3 for _ in range(n)]
    dp[0] = v[0].copy()
    for i in range(1, n):
        for j in range(3):
            for k in range(3):
                if j == k: continue
                dp[i][j] = max(dp[i][j], dp[i-1][k]+v[i][j])
    print(max(dp[n-1]))
edu_dp_c_vacation()