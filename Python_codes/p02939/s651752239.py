def main():
    word = list(input())
    dp = [0] * len(word)
    dp[0] = 1
    dp[1] = 1
    if word[0] != word[1]:
        dp[1] = 2
    for i in range(2, len(word)):
        if word[i] != word[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 3] + 2
    print(dp[len(word) - 1])


if __name__ == '__main__':
    main()

