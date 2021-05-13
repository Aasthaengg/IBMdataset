nums = []
while True:
    num = int(input())
    if num==0:
        break
    nums.append(num)

for i in range(len(nums)):
    print("Case " + str(i+1) + ": " + str(nums[i]))
    
