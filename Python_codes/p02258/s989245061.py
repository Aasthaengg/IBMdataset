N = input()
nums = []
for i in range(N):
     nums.append(input())
profit = nums[1] - nums[0]
min = nums[0]
for a in range(1, N):
     if nums[a] - min > profit:
          profit = nums[a] - min

     if nums[a] < min:
               min = nums[a]
print profit