N = int(input())
S = str(input())

dp = [[0 for _ in range(N)] for _ in range(N)]
#dp[i][j]:= i 文字目からと j 文字目からとで一致する最長の長さ
#(この時点では文字列がかぶっても OK とする)

for i in range(N):
  for j in range(i+1,N):
    if S[i] != S[j]:
      dp[i][j] = 0
    else:
      if i == 0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j-1]+1
ans = 0
for i in range(N):
  for j in range(N):
    temp = min(dp[i][j],j-i)
    ans = max(ans,temp)
print(ans)