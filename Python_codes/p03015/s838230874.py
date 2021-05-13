MOD = 10**9 +7

def main():
    l=input()
    n=len(l)

    dp=[[0]*2 for _ in range(n)]
    dp[0][0] = 2
    dp[0][1] = 1 

    for i in range(1,n):
        if l[i]=='0':
            dp[i][0] = dp[i-1][0]
            dp[i][1] = 3*dp[i-1][1]
            dp[i][1] %= MOD
        else:
            dp[i][0] = 2*dp[i-1][0]
            dp[i][0] %= MOD
            dp[i][1] = dp[i-1][0] + 3*dp[i-1][1]
            dp[i][1] %= MOD
    
    print(sum(dp[-1])%MOD)
if __name__=='__main__':
    main()