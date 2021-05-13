def getval():
    n = int(input())
    p = list(map(float,input().split()))
    return n,p

def main(n,p):
    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    dp[1][1] = p[0]
    dp[1][0] = 1 - p[0]
    for i in range(2,n+1):
        locp = p[i-1]
        for j in range(n+1):
            dp[i][j] = dp[i-1][j] * (1 - locp)
            if j>0:
                dp[i][j] += dp[i-1][j-1] * locp
    print(sum(dp[n][(n+1)//2:]))
    #print(dp)

if __name__=="__main__":
    n,p= getval()
    main(n,p)  
