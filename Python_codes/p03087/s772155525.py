n,q = map(int ,input().split())
s = input()

nums = [0]*len(s)
for i in range(1,n):
  if s[i-1] == "A" and s[i] == "C": nums[i] = nums[i-1] + 1
  else: nums[i] = nums[i-1]

for _ in range(q):
  l,r = map(lambda x: int(x)-1, input().split())
  print(nums[r]-nums[l])