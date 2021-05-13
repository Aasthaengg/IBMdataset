ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
a=nl()

ans=0

nums = dict()

for i in range(n):
  num_i = i+a[i]
  if num_i not in nums:
    nums[num_i]=0
  nums[num_i]+=1

for j in range(n):
  num_j = j-a[j]
  if num_j in nums:
    ans+=nums[num_j]

print(ans)