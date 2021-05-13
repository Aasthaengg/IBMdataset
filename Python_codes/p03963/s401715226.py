nums = [int(e) for e in input().split()]
val = nums[1]
for i in range(nums[0]-1):
    val = val*(nums[1]-1)
print(val)
