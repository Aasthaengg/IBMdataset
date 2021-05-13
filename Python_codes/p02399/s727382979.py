
nums = [int(e) for e in input().split()]
a = int(nums[0]/nums[1])
b = int(nums[0]%nums[1])
c = "{:.5f}".format(nums[0]/nums[1])
print(a,b,c)

