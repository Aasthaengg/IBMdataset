def main():
    s = input()
    n = len(s)
    inf = pow(10, 9)+7
    
    dp = [[0]*13 for i in range(n)]
    if s[0] == "?":
        for i in range(10):
            dp[0][i] = 1
    else:
        dp[0][int(s[0])] = 1
    
    for i in range(1, n):
        if s[i] != "?":
            k = int(s[i])
            for j in range(13):
                dp[i][(10*j+k)%13] += dp[i-1][j]
        else:
            for k in range(10):
                for j in range(13):
                    dp[i][(10*j+k)%13] += dp[i-1][j]
        for j in range(13):
            dp[i][j] %= inf
        
    print(dp[n-1][5])
    

if __name__ == "__main__":
    main()