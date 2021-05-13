n = int(input())

if n == 1:
  print(1)
  exit()
  
nums = [0]*(n+1)
nums[0] = 2
nums[1] = 1

for i in range(2,n+1):
  nums[i] = nums[i-1]+nums[i-2]
print(nums[n])