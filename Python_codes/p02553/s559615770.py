nums = list(map(int,input().split()))

ans = []
for x in range(2):
	for y in range(2,4):
		ans.append(nums[x]*nums[y])	 
print(max(ans))
