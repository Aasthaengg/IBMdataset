n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
low, high = 0, max(arr) + 1
while high - low > 1:
  mid = (high + low) // 2
  curr = 0
  for i in arr:
    curr += (i - 1)//mid
  if curr > k:
    low = mid
  else:
    high =  mid
print(high)    