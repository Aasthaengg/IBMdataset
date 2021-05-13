nums = list(map(int, input().split()))
nums.sort()
ans = 0
for i in range(1, 3):
    ans += nums[i] - nums[i - 1]
print(ans)