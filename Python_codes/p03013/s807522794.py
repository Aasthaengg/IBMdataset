N,M = map(int,input().split())
A = set([]); MOD = pow(10,9)+7
for i in range(M):
  a = int(input())
  A.add(a-1)
dp = [[0]*2 for _ in range(N)] #dp[i][j] i段目(0index)にj=0最後1段でj=1最後2段できた。
if 0 not in A:
  dp[0][0] = 1
if N == 1:
  print(sum(dp[0]))
  exit()
if 1 not in A:
  dp[1][0] = dp[0][0]+dp[0][1]
  dp[1][1] = 1
for i in range(2,N):
  if i in A:
    continue
  dp[i][0] = (dp[i-1][0]+dp[i-1][1])%MOD
  dp[i][1] = (dp[i-2][0]+dp[i-2][1])%MOD
ans = sum(dp[N-1])%MOD
#print(dp)
print(ans)