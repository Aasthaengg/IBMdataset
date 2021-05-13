def main():
    platform_count = int(input())
    platforms = [int(x) for x in input().split()]

    dp = [0] * platform_count
    for i in range(platform_count):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = abs(platforms[i] - platforms[i - 1])
        else:
            dp[i] = min(
                abs(platforms[i] - platforms[i - 1]) + dp[i - 1],
                abs(platforms[i] - platforms[i - 2]) + dp[i - 2])
    print(dp[platform_count - 1])


if __name__ == '__main__':
    main()
