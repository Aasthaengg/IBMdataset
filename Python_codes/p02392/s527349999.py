nums=list(map(int,input().split()))

if nums[2] > nums[1] and nums[1] > nums[0]:
	print("Yes")
else:
	print("No")