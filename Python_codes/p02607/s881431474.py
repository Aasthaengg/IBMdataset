N = int(input())
nums = [int(i) for i in input().split(' ')]
count = 0
for i in range(0,N,2):
  if nums[i] % 2 != 0:
    count += 1
print(count)