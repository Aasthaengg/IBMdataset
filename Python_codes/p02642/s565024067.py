N = int(input())
nums = list(map(int, input().split()))
nums.sort()
checked = [0 for _ in range(nums[-1]+1)]
answer = 0
for i in range(N-1):
  if checked[nums[i]] == 1:
    continue
  else:
    if nums[i] != nums[i+1]:
      answer += 1
    count = 1
    temp = nums[i]
    while(temp <= nums[-1]):
      checked[temp] = 1
      count += 1
      temp= nums[i]*count
if checked[nums[-1]] == 0:
  answer += 1
print(answer)