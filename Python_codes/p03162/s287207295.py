def solve(n,a,b,c):
    dp = [[0]*3 for _ in range(n)]

    #dp[][0] = a, dp[][1] = b, dp[][2] = c
    dp[0][0] = a[0]
    dp[0][1] = b[0]
    dp[0][2] = c[0]
    for i in range(1,n):
        for j in range(3):
            if j == 0:
                dp[i][j] = max(dp[i-1][1],dp[i-1][2]) + a[i]
            if j == 1:
                dp[i][j] = max(dp[i-1][0],dp[i-1][2]) + b[i]
            if j == 2:
                dp[i][j] = max(dp[i-1][0],dp[i-1][1]) + c[i]

    print(max(dp[n-1]))








if __name__ == '__main__':
    n = int(input())
    a = []
    b = []
    c = []
    for i in range(n):
        t1,t2,t3 = map(int,input().split())
        a.append(t1)
        b.append(t2)
        c.append(t3)

    solve(n,a,b,c)