n = int(input())
dp = [0, 0]
for c in input():
    if c == '.':
        dp[1] += 1
    else:
        dp[1] = min(dp[1], dp[0])
        dp[0] += 1
print(min(dp))