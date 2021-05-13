n = int(input())
sum = 1
flag = 1
limit = 1000000000000000000
nums = list(map(int, input().split()))
for num in nums:
  if num == 0:
    sum = 0
    break;
  if flag == 1:
    sum *= num
  if sum > limit or sum == -1:
    flag = 2
    sum = -1
print(sum)