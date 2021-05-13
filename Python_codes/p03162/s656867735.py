N = int(input())
dp = [0, 0, 0]
for _ in range(N):
    a, b, c = map(int, input().split())
    dp = [a+max(dp[1], dp[2]), b+max(dp[0], dp[2]), c+max(dp[0], dp[1])]
print(max(dp))