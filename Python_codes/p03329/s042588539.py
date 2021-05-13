N = int(input())

lst = [1]
i = 1
while 6**i <= N:
  lst.append(6**i)
  i += 1
i = 1
while 9**i <= N:
  lst.append(9**i)
  i += 1

lst.sort()

dp = [100001]*(N+1)
dp[0] = 0
for i in range(1,N+1):
  for k in lst:
    if i - k >= 0:
      dp[i] = min(dp[i],dp[i-k]+1)
      
print(dp[N])