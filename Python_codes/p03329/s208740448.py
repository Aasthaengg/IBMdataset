n = int(input())

dp = [float('inf')] * (n + 1)
dp[0] = 0
nums = [1]
i = 1
while 6 ** i <= n:
    nums.append(6 ** i)
    i += 1
i = 1
while 9 ** i <= n:
    nums.append(9 ** i)
    i += 1
nums.sort()
for i in range(n + 1):
    for j in range(len(nums)):
        num = nums[j]
        if i - num >= 0:
            dp[i] = min(dp[i], dp[i - num] + 1)
ans = dp[n]
print(ans)
