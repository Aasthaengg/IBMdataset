N = int(input())
a = list(map(int, input().split()))

A =[] 

for i in range(N):
  A.append([i+1,a[i]])


A.sort(key=lambda x: x[1], reverse=True)


dp = [[0] * (N+1) for i in [1] * (N+1)]


for i in range(N+1):
  for x in range(i+1):
    y = i - x
    if x == 0 and y == 0:
      dp[x][y] = 0
    
    elif x == 0:
      dp[x][y] = dp[x][y-1] + A[y-1][1]*((N-y+1) - (A[y-1][0]))


    elif y == 0:
      dp[x][y] = dp[x-1][y] + A[x-1][1]*((A[x-1][0]) - x )


    else:
      dp[x][y] = max(dp[x][y-1] + A[x+y-1][1]*((N-y+1) - (A[x+y-1][0])) , dp[x-1][y] + A[x+y-1][1]*((A[x+y-1][0]) - x ))

ans = 0
for x in range(N+1):
  y = N - x
  ans = max(ans,dp[x][y])
  
print(ans)