N, M = map(int, input().split())

nums = [1, 2]
for i in range(2, N+1):
  plus = nums[i-2] + nums[i-1]
  nums.append(plus)
  
stairs = [0]*N
stairs[0] = 1
stairs.append(1)
flag = True
for i in range(M):
  m = int(input())
  if stairs[m] == 1:
    flag = False
    break
  else:
    stairs[m-1], stairs[m], stairs[m+1] = 1, 1, 1
  
ans = 1
mode = False
left = -1
right = -1
for i in range(N+1):
  if stairs[i] == 0:
    if not mode:
      left = i
      mode = True
  else:
    if mode:
      right = i
      n = right - left
      ans *= nums[n]
      mode = False
      
if flag:
  print(ans%(10**9+7))
else:
  print(0)