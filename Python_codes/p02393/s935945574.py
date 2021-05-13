nums = [int(e) for e in input().split()]
for i in range(len(nums)):
    for j in range(i):
        if nums[i]<nums[j]:
            a = nums[i]
            nums[i] = nums[j]
            nums[j] = a

nums_2 = " ".join(map(str, nums))
print(nums_2)
