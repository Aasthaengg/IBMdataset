nums = [int(e) for e in input().split()]

count=0
for i in range(nums[0]+1):
    for j in range(nums[0]+1):
        if 0<=nums[1]-i-j<=nums[0]:
            count=count+1

print(count)
