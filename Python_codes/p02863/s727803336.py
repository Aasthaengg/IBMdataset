from itertools import accumulate

n,t = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
dp1 = [[-(10 ** 18)] * t for i in range(n)]
dp2 = [[-(10 ** 18)] * t for i in range(n)]
dp1[0][0] = 0
dp2[0][0] = 0
for i,(a,b) in enumerate(ab[:-1]):
  for j in range(t):
    dp1[i+1][j] = max(dp1[i+1][j],dp1[i][j])
    if j < t-a:
      dp1[i+1][j+a] = max(dp1[i+1][j+a],dp1[i][j]+b)
for i,(a,b) in enumerate(ab[n-1:0:-1]):
  for j in range(t):
    dp2[i+1][j] = max(dp2[i+1][j],dp2[i][j])
    if j < t-a:
      dp2[i+1][j+a] = max(dp2[i+1][j+a],dp2[i][j]+b)
ans = 0
for key,(i,j,(a,b)) in enumerate(zip(dp1,dp2[::-1],ab)):
  nowi,nowj = 0,0
  I,J = [],[]
  for x,y in zip(i,j):
    nowi = max(nowi,x)
    nowj = max(nowj,y)
    I.append(nowi)
    J.append(nowj)
  J.reverse()
  tmp = 0
  for x,y in zip(I,J):
    tmp = max(tmp,x+y)
  tmp += b
  ans = max(ans,tmp)
print(ans)