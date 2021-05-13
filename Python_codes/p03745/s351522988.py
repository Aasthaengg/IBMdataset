N = int(input())
nums = list(map(int, input().split()))
upper = True
lower = True
before = nums[0]
answer = 0
for i, num in enumerate(nums):
  if before < num:
    lower = False
  elif before > num:
    upper = False
  before = num
  if not upper and not lower:
    answer += 1
    upper = True
    lower = True
print(answer+1)