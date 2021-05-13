nums = list(map(int,input().split()))
A = nums[0]
B = nums[1]
if abs(A-B) % 2 != 0:
  print("IMPOSSIBLE")
else:
  mini = min(A,B)
  print((A+B)//2)