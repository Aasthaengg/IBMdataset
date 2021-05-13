def main():
    n = int(input())
    coins = list(map(float,input().split()))
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    dp[0][0] = 1
        
    for pos in range(1,n+1):
        for heads in range(pos+1):
            if heads == 0:
                dp[pos][heads] = dp[pos-1][heads]*(1-coins[pos-1])
            else:
                dp[pos][heads] = dp[pos-1][heads]*(1-coins[pos-1])
                dp[pos][heads] += dp[pos-1][heads-1]*coins[pos-1]

    
    print(sum(dp[-1][(n+1)//2:]))

main()
