def divide(iterable):
	return list(map((lambda x : x // 2),iterable))
    
N = int(input())
nums = list(map(int, input().split()))
count = 0
flag = 0
while 1:
  if flag == 1:
    break
  for num in nums:
    if num % 2 == 1:
      flag = 1
      break
  else:
    count += 1
    nums = divide(nums)
print(count)