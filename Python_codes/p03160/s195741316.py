def solve(N, h):
    dp = [float('inf') for i in range(N+1)]
    dp[1] = 0
    for i in range(1, N+1):
        if i+1 <= N:
            dp [i+1] = min(dp[i+1],dp[i] + abs(h[i+1]-h[i]))
        if i+2 <= N:
            dp [i+2] = min(dp[i+2],dp[i] + abs(h[i+2]-h[i]))
    return dp[N]
N = int(input())
h = [0] + list(map(int, input().split()))
print(solve(N, h))