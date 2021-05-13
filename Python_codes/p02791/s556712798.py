N = int(input())
nums = list(map(int, input().split()))
before_min = 10**6
answer = 0
for num in nums:
  if num <= before_min:
    answer += 1
    before_min = min(before_min, num)
print(answer)