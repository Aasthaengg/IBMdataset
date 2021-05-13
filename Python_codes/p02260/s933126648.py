N = int(raw_input())
nums = map(int, raw_input().split(" "))

count = 0
for i in range(0, len(nums)):
    mini = i
    for j in range(i, len(nums)):
        if nums[mini] > nums[j]:
            mini = j
    if i != mini:
        count += 1
    temp = nums[i]
    nums[i] = nums[mini]
    nums[mini] = temp


nums = map(str, nums)
print(" ".join(nums))
print(count)