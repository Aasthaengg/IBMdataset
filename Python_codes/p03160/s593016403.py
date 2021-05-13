n = int(input())
h = list(map(int, input().split()))

dp = [0, abs(h[0] - h[1])]

for i in range(2, n):
    small_jump = dp[i - 1] + abs(h[i] - h[i - 1])
    big_jump = dp[i - 2] + abs(h[i] - h[i - 2])
    dp.append(min(small_jump, big_jump))

print(dp[-1])
