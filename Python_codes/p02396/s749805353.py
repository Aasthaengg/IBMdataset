nums = []
num = input()

while num != 0:
	nums.append(num)
	num = input()

for i in range(len(nums)):
	print "Case %d: %d" %(i + 1, nums[i])