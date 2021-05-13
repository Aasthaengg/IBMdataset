N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A_dp = [0] * (N + 1)
B_dp = [0] * (M + 1)

for i in range(1,N+1):
  if i == 1:
    A_dp[i] += A[i-1]
    continue
  A_dp[i] += A_dp[i-1] + A[i-1]
  
for j in range(1,M+1):
  if j == 1:
    B_dp[j] += B[j-1]
    continue
  B_dp[j] += B_dp[j-1] + B[j-1]
  
cnt = 0
j = M

for i in range(N+1):
  if A_dp[i] > K:
    continue
  while A_dp[i] + B_dp[j] > K:
    j -= 1
  cnt = max(cnt, i+j)
  
print(cnt)