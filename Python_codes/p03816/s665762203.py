N = int(input())
nums = list(map(int, input().split()))
unit = set(nums)
if len(unit)%2 == 0:
  print(len(unit)-1)
else:
  print(len(unit))