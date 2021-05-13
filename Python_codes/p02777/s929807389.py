a = [i for i in input().split()]
nums = [int(i) for i in input().split()]
thr = input()
if(thr == a[0]):
	nums[0] -= 1
else:
	nums[1] -= 1
print(nums[0],nums[1])