N = int(input())
nums = list(map(int, input().split()))
answer = 0
for i, num in enumerate(nums, start=1):
  if i == nums[num-1] and i < num:
    answer += 1
print(answer)
