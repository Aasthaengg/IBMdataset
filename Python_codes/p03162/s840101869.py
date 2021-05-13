N = int(input())
dp = [0, 0, 0]
for i in range(N):
    a, b, c = map(int, input().split())
    tmp_a = a + max(dp[1], dp[2])
    tmp_b = b + max(dp[0], dp[2])
    tmp_c = c + max(dp[0], dp[1])
    dp = [tmp_a, tmp_b, tmp_c]
print(max(dp))
