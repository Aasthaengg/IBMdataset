nums = input().split()

#print(nums)
index = 0
for num in nums:
    index += 1
    if num == "0":
        print(index)
        break
