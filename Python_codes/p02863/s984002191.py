import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
n,t = map(int,readline().split())
f = []
m = 0
for i in range(n):
  p,q = map(int,readline().split())
  m = max(m,p)
  f.append((p,q))
  
f.sort()
dp = [[0]*(t+m) for i in range(n+1)]

for i,c in enumerate(f):
  a,b = c
  for j in range(t+m):
    if j-a >= t:
      break
    if j < a :
      dp[i+1][j] = dp[i][j]
    else:
      dp[i+1][j] = max(dp[i][j],dp[i][j-a]+b)
      
print(max(dp[n]))
