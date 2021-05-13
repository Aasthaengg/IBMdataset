

def tc():
    n = int(input())
    stones = list(map(int, input().split()))
    # dp[i]: min cost to get to stone i (0 based)
    dp = [0] * n
    dp[1] = abs(stones[1] - stones[0])

    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(stones[i] - stones[i - 1]),
                    dp[i - 2] + abs(stones[i] - stones[i - 2]))

    print(dp[-1])


tc()
