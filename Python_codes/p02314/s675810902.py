def main():
    n, m = map(int, input().split())
    
    INF = float('inf')
    dp = [[INF for i in range(n+1)] for j in range(m+1)]
    
    for i, c in enumerate(list(map(int, input().split()))):
        i += 1
        for j in range(1, n+1):
            if c == j:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j - c >= 0: dp[i][j] = min(dp[i][j], dp[i][j-c]+1)
    print(dp[-1][-1])

if __name__ == '__main__':
    main()
