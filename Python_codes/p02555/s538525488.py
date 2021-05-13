
def main():
    mod = 10**9 + 7
    s = int(input())
    dp = [0] * (s+3)
    dp[0] = 1
    for i in range(0,len(dp)):
        for j in range(i+3,len(dp)):
            dp[j] = dp[j] + dp[i]

    print(dp[s]%mod)




if __name__ == '__main__':
    main()
