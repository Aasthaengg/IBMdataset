N = int(input())
A = list(map(int,input().split()))
 
ans = 1
mode = 0
for i in range(N-1):
  if mode == 0:
    if A[i] < A[i+1]:
      mode = 1
    elif A[i] > A[i+1]:
      mode = -1
    else:
      mode = 0
  if mode == 1:
    if A[i] > A[i+1]:
      ans += 1
      mode = 0
  elif mode == -1:
    if A[i] < A[i+1]:
      ans += 1
      mode = 0
  else:
    pass
print(ans)