nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
x, y = map(int, input().split())
if nums[x - 1] == nums[y - 1] :
  print("Yes")
else :
  print("No")