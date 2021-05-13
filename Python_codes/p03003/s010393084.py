import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    s = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]
    
    mod = pow(10, 9)+7
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(m+1):
        dp[0][i] = 1
    
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = (dp[i+1][j]+dp[i][j+1]-dp[i][j])%mod
            if s[i] == t[j]:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= mod
    
    print(dp[n][m])            
    
if __name__ == "__main__":
    main()