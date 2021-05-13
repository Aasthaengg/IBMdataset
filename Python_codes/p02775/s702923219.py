def main():
    s = list(str(input()))
    s.reverse()
    for i in range(len(s)):
        s[i] = int(s[i])
    s += [0]
    m = len(s)

    dp = [[10**7, 10**7] for _ in range(len(s)+5)]
    # dp[i][0]: 繰り下がりなし
    # dp[i][1]: 繰り下がりあり

    dp[0][0] = 0

    for i in range(m):
        for j in range(2):
            nd = s[i]
            if j == 1:
                nd += 1
            if dp[i+1][0] >= dp[i][j]+nd:
                dp[i+1][0] = dp[i][j]+nd
            if dp[i+1][1] >= dp[i][j]+10-nd:
                dp[i+1][1] = dp[i][j]+10-nd
    #print(dp)
    print(dp[m][0])

if __name__ == '__main__':
    main()