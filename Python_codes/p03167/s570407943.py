def solve(n,m,ar):
    mod = int(1e9) + 7
    dp = [[0] * (m+2) for _ in range(n+2)]
    dp[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if ar[i][j] == "#": continue
            if i == 1 and j == 1: continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod

    print(dp[n][m])



if __name__ == '__main__':
    n,m = map(int,input().split())

    ar = [[-1] * (m+2) for i in range(n+2)]

    for i in range(1,n+1):
        temp = list(input())
        for j in range(1,m+1):
            ar[i][j] = temp[j-1]

    solve(n,m,ar)