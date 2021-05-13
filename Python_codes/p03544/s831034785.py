N=int(input())
nums=[2, 1]
for _ in range(N-1):
  nums=[nums[1], nums[0]+nums[1]]
print(nums[1])