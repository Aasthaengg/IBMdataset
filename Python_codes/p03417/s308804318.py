nums=list(map(int, input().split()))
nums.sort()
if nums[0]==1:
  if nums[1]==1:
    print(1)
  else:
    print(nums[1]-2)
elif nums[0]==2:
  print(0)
else:
  print((nums[0]-2)*(nums[1]-2))