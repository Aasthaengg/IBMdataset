N = int(input())
nums = list(map(int, input().split()))
count = 0
for i in range(N):
  if nums[i]%2 == 1:
    count += 1
if count%2 == 1:
  print("NO")
else:
  print("YES")