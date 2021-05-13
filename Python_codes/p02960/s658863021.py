def main():
    s=input()
    n = len(s)
    dp = [[0]*(13) for _ in range(100005)]
    MOD = 10**9 + 7
    dp[0][0]=1

    for i in range(n):
        c=0
        if(s[i]=="?"):c=-1
        else:c = int(s[i])

        for j in range(10):
            if(c!=-1 and c!=j):
                continue
            for ki in range(13):
                dp[i+1][(ki*10+j)%13] += dp[i][ki]

        for j in range(13):
            dp[i+1][j]%=MOD
    res = dp[n][5]

    print(res)





if __name__ == '__main__':
    main()
