n = int(input())
nums = list(map(int, input().split()))
if n == 0:
  if nums[0] == 1:
    print(1)
  else:
    print(-1)
  exit()
if n > 0 and nums[0] != 0:
  print(-1)
  exit()
n_nods = 1
ans = 1
ret = sum(nums)
for i in range(1,n+1):
  n_nods = min(n_nods*2,ret)
  ans += n_nods
  ret -= nums[i]
  n_nods -= nums[i]
  if n_nods < 0:
    print(-1)
    exit()
  if n_nods == 0 and i < n:
    print(-1)
    exit()
print(ans)