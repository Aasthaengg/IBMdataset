def main():
    platform_count, jumping_power = [int(x) for x in input().split()]
    platforms = [int(x) for x in input().split()]
    dp = [0]
    for i in range(1, platform_count):
        indexes = (i - x for x in range(1, jumping_power + 1) if i - x >= 0)
        dp.append(
            min(abs(platforms[i] - platforms[before]) + dp[before]
                for before in indexes))
    print(dp[platform_count - 1])


if __name__ == '__main__':
    main()
