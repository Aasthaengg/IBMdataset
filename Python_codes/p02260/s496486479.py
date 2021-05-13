def selectionSort(nums, length):
  count = 0
  for i in xrange(length):
    minj = i
    for j in xrange(i, length):
      # print "i = %d, j = %d, minj = %d, count = %d" % (i, j, minj, count)
      # print nums
      if nums[j] < nums[minj]:
        minj = j
    nums[i], nums[minj] = nums[minj], nums[i]
    count += 1 if i != minj else 0
  return [nums, count]

length = int(raw_input())
nums = map(int, raw_input().split())
ans = selectionSort(nums, length)

print " ".join(map(str, ans[0]))
print ans[1]