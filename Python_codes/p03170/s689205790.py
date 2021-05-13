n,k = map(int,input().split())
a = list(map(int,input().split()))
dp = [False]*(k+1)
i = a[0]
for i in range(a[0],k+1):
  for j in range(n):
    if i-a[j] < 0:
      break
    if dp[i-a[j]] == False:
      dp[i] = True
      break
print(["Second","First"][dp[k]])