import itertools

N,MA,MB = map(int,input().split())
arr = []

for i in range(N):
  l = list(map(int,input().split()))
  arr.append(l)
  
dp = [ [ [50000 for k in range(401)] for j in range(401)] for i in range(N+1) ]
dp[0][0][0] = 0
ans = 50000

for i,a,b in itertools.product(range(1,N+1),range(401),range(401)):
  A = arr[i-1][0]
  B = arr[i-1][1]
  C = arr[i-1][2]
  
  if A <= a and B <= b and dp[i-1][a-A][b-B] != 50000:
    dp[i][a][b] = min(dp[i-1][a][b],dp[i-1][a-A][b-B] + C)
  else:
    dp[i][a][b] = dp[i-1][a][b]

for a,b in itertools.product(range(401),range(401)):
    if a * MB == b * MA and a != 0 and b != 0:
      ans = min(ans,dp[-1][a][b])
    
if ans == 50000:
  print(-1)
else:
  print(int(ans))