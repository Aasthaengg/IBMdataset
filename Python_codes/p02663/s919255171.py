string = input()
nums = string.split(' ')

hour = int(nums[2]) - int(nums[0])
minute = int(nums[3]) - int(nums[1])
time = hour * 60 + minute - int(nums[4])

print(time)
