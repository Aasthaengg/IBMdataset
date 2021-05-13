nums = list(map(int, input().split()))
nums.sort(reverse=True)
ans = nums[0] * 10 + sum(nums[1:])
print(ans)
