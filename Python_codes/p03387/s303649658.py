nums = list(map(int, input().split()))
nums.sort()
count = nums[2] - nums[1]
nums[0] += nums[2] - nums[1]
if (nums[2]-nums[0])%2 == 0:
  count += (nums[2]-nums[0])//2
else:
  count += (nums[2]-nums[0])//2 + 2
print(count)