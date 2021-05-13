N, K = map(int, input().split())
h = [0] + list(map(int, input().split()))

dp = [10 ** 9] * (N + 1)
dp[1] = 0

for i in range(2, N + 1):
    for j in range(max(1,i-K), i):
        # print(i,j)
        dp[i] = min(dp[i], dp[j] + abs(h[i] - h[j]))

print(dp[-1])
# print(dp)
