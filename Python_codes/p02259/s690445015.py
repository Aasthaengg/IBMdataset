def bubbleSort(nums, length):
  count = 0
  flag = 1
  while flag:
    flag = 0
    for j in xrange(length - 1, 0, -1):
      if nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        count += 1
        flag = 1
  return [nums, count]

length = int(raw_input())
nums = map(int, raw_input().split())
ans = bubbleSort(nums, length)
print " ".join(map(str, ans[0]))
print ans[1]