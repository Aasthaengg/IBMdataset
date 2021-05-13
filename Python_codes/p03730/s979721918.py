nums = [int(e) for e in input().split()]
count=0
for i in range(nums[1]):
    if (nums[0]*(i+1))%nums[1]==nums[2]:
        count=1
if count==0:
    print("NO")

else:
    print("YES")
