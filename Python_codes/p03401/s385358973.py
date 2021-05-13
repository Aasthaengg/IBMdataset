N = int(input())
A = list(map(int, input().split()))
A.append(0)

ans = [None] * (N+1)
ans[0] = abs(0 - A[0])
for i in range(N):
  ans[i+1] =  abs(A[i] - A[i+1])
  
ansS = sum(ans)

for i in range(N):
  if i == 0:
    tmp = abs(A[1])
  else:
    tmp = abs(A[i+1] - A[i-1])
  print(ansS - ans[i] - ans[i+1] + tmp)