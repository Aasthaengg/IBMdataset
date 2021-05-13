nums = list(map(int, input().split()))
nums.sort()
if nums[0] != nums[1]:
  print(nums[0])
else:
  print(nums[-1])