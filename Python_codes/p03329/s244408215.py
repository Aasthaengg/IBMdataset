def main():
    N = int(input())

    #6**6=46656, 6**7=279936
    #9**5=59049, 9**6=531441
    list = [1]
    list.extend([6 ** i for i in range(1, 7)])
    list.extend([9 ** i for i in range(1, 6)])

    dp = [float("inf")] * 100001
    dp[0] = 0

    for i in range(N+1):
        for j in list:
            if i + j > 100000:
                continue
            else:
                dp[i+j] = min(dp[i+j], dp[i]+1)

    print(dp[N])

if __name__ == "__main__":
    main()

