nums=list(map(int, input().split()))
ans=[]
for i in range(2):
  ans.append(nums[i]*nums[2])
  ans.append(nums[i]*nums[3])
print (max(ans))