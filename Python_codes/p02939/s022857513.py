S = input()

dp = [[0 for _ in range(4)] for _ in range(len(S))]

dp[0][0] = 1
dp[1][1] = 1
for i in range(1, len(S)):

  # 直前1文字 次1文字
  if S[i-1] != S[i]:
    dp[i][0] = max(dp[i-1][0], dp[i-1][2]) + 1

  # 直前1文字 次2文字
  if i < len(S) - 1:
    dp[i+1][1] = max(dp[i-1][0], dp[i-1][2]) + 1

  # 直前2文字 次1文字
  dp[i][2] = max(dp[i-1][1], dp[i-1][3]) + 1

  # 直前2文字 次2文字
  if  2 <= i < len(S)-1 and (S[i-2] != S[i] or S[i-1] != S[i+1]):
    dp[i+1][3] =  max(dp[i-1][1], dp[i-1][3]) + 1


print(max(dp[-1]))
    

