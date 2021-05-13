

def tc():
    n, k = map(int, input().split())
    stones = list(map(int, input().split()))
    # dp[i]: min cost to get to stone i (0 based)
    INF = float('inf')
    dp = [INF] * n
    dp[0] = 0

    # since from one stone you can go to many
    # try using push dp instead of pull
    for i in range(n):
        for j in range(k + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + abs(stones[i + j] - stones[i]))

    print(dp[-1])


tc()
