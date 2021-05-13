N, K = map(int, input().split())
h = [int(i) for i in input().split()]
dp = [10**6] * 100005
dp[0] = 0
# dp[1] = abs(h[1]-h[0])
for i in range(1, N):
    dp[i] = min(dp[i-j] + abs(h[i-j] - h[i]) for j in range(1,min(K,i)+1))
    # print([dp[i-j] + abs(h[i-j] - h[i]) for j in range(1,min(K,i)+1)])
    # for j in range(1, min(K,i)+1):
    #     dp[i] = min(dp[i], dp[i-j] + abs(h[i-j] - h[i]))

print(dp[N-1])