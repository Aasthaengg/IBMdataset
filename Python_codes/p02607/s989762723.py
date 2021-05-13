n = int(input())
nums = [int(x) for x in input().split()]
nums_v2 = []
nums_v3 = []

for i in range(len(nums)):
      if (i+1)%2 == 1:
            nums_v2.append(nums[i])

for i in range(len(nums_v2)):
      if nums_v2[i]%2 == 1:
            nums_v3.append(nums_v2[i])

print(len(nums_v3))