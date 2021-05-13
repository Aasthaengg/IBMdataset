n = int(input())
A = [int(input()) for _ in range(n)]

ans = 0
if A[0] != 0:
  ans = -1
else:
  pre = 0
  for i in range(1,n):
    if A[i] == pre+1:
      ans += 1
      pre = A[i]
    elif A[i] == pre:
      ans += A[i]
    elif A[i] <= pre-1:
      ans += A[i]
      pre = A[i]
    else:
      ans = -1      
      break
      
print(ans)