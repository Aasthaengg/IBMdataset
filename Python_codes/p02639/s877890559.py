nums = list(map(int, input().split()))
res = 1
for i in range(5):
  if nums[i] != i + 1:
    res = i + 1
print(res)