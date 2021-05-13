nums = input().split()
num1 = int(nums[0])
num2 = int(nums[1])
num3 = int(nums[2])
for x in nums:
    if nums.index(x)+1 < len(nums):
        if x != nums[nums.index(x)+1] and x != nums[nums.index(x)-1]:
            print(x)
    else:
        if x != nums[0] and x != nums[1]:
            print(x)