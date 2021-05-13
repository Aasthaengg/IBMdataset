S=input()
dp=[[0 for i in range(len(S))] for j in range(2)]
if len(S)==1:
    print(S)
    exit()
dp[0][0]=int(S[0])
dp[1][0]=int(S[0])-1
for i in range(len(S)-1):
    dp[0][i+1] = dp[0][i]+int(S[i+1])
    dp[1][i+1] = max(dp[0][i]+int(S[i+1])-1,dp[1][i]+9)
print(max(dp[1][len(S)-1],dp[0][len(S)-1]))