n, k = list(map(int, input().split()))
costs = list(map(int, input().split()))

if k > n:
    k == n

if n == 2:
    print(abs(costs[-1] - costs[-2]))
else:
    dp = [float("inf") for i in range(n)]
    dp[-1] = 0

    for i in range(1, k + 1):
        curr_min = float("inf")
        for j in range(i):
            curr_min = min(abs(costs[n - i - 1] - costs[n - j - 1]) + dp[n - j - 1], curr_min)
        dp[n - i - 1] = curr_min    

    for i in range(n - k - 2, -1, -1):
        curr_min = float("inf")
        for j in range(1, k + 1):
            curr_min = min(curr_min, abs(costs[i] - costs[i + j]) + dp[i + j]) 
        dp[i] = curr_min

    print(dp[0])
