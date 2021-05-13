def resolve():
    n = int(input())
    c = [int(input()) for i in range(n)]
    lac = [-1]* 200010
    dp = [0]*n

    dp[0] = 1
    lac[c[0]] = 0
    for i in range(1, n):
        if c[i] == c[i-1]:
            dp[i] = dp[i-1]
        elif lac[c[i]] == -1:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[lac[c[i]]]
        lac[c[i]] = i
    print(dp[n-1]%(10**9+7))
resolve()