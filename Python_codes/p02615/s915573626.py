N = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
score = nums[0] + 2 * sum(nums[1:N//2])
if N%2 != 0:
  score += nums[N//2]
print(score)