n,m = map(int, input().split())
ka = [list(map(int, input().split())) for _ in range(n)]

nums = [0]*m
for i in ka:
  for j in range(1,i[0]+1):
    nums[i[j]-1] += 1
print(nums.count(n))