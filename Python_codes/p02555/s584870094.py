def main():

    s = int(input())

    dp = [0] * 2001
    dp[3] = 1
    dp[4] = 1
    dp[5] = 1
    dp[6] = 2
    dp[7] = 3
    dp[8] = 4
    if s < 9:
        print(dp[s])
        return
    M = 10 ** 9 + 7
    total = sum(dp[:7]) + 1
    for i in range(9, s+1):
        dp[i] = total
        total += dp[i-2]
    print(dp[s] % M)
    return


if __name__=='__main__':
    main()
