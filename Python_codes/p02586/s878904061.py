R, C, K = map(int, input().split())

mp = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
  r,c,v = map(int, input().split())
  mp[r][c] = v

memo = [[0]*4 for _ in range(R+1)]

for j in range(1,C+1):
  for i in range(1,R+1):
    if mp[i][j] > 0:
      memo[i][3] = max(memo[i][3], memo[i][2] + mp[i][j])
      memo[i][2] = max(memo[i][2], memo[i][1] + mp[i][j])
      memo[i][1] = max(memo[i][1], memo[i][0] + mp[i][j], max(memo[i-1])+mp[i][j])
      memo[i][0] = max(memo[i][0], max(memo[i-1]))
    else:
      memo[i][0] = max(memo[i][0], max(memo[i-1]))
      
print(max(memo[R]))