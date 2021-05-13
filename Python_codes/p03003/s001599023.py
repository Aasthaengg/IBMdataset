import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n,m = map(int,readline().split())
mod = 10**9+7
a = [0]+[int(i) for i in readline().split()]
b = [0]+[int(i) for i in readline().split()]
dp = [[0]*(m+1) for i in range(n+1)]
su = [[0]*(m+1) for i in range(n+1)]

dp[0][0] = 1
su[0][0] = 1
for i in range(1,n+1):
  su[i][0] = 1
for j in range(1,m+1):
  su[0][j] = 1
  
for i in range(1,n+1):
  for j in range(1,m+1):
    if a[i] == b[j]:
      dp[i][j] = su[i-1][j-1]
    else:
      dp[i][j] = 0
    su[i][j] = su[i-1][j]+su[i][j-1]-su[i-1][j-1]+dp[i][j]
    su[i][j] %= mod
    
print(su[n][m])