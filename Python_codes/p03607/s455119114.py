N = int(input())
nums = {}
for i in range(N):
    n = int(input())
    if n in nums.keys():
        nums[n] += 1
    else:
        nums[n]=1
c = 0
for te in nums.values():
   if te % 2 == 1:
       c+=1
print(c)
