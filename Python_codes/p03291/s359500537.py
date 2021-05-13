S = input()

MOD = 10**9+7
dp = [[0 for _ in range(4)]for _ in range(len(S)+1)]
dp[0][0] = 1

for ind,i in enumerate(S):
    if(i=='A'):
        dp[ind+1][0] = dp[ind][0]
        dp[ind+1][1] = dp[ind][1] + dp[ind][0]
        dp[ind+1][2] = dp[ind][2]
        dp[ind+1][3] = dp[ind][3]
    elif(i=='B'):
        dp[ind+1][0] = dp[ind][0]
        dp[ind+1][1] = dp[ind][1]
        dp[ind+1][2] = dp[ind][2] + dp[ind][1]
        dp[ind+1][3] = dp[ind][3]
    elif(i=='C'):
        dp[ind+1][0] = dp[ind][0]
        dp[ind+1][1] = dp[ind][1]
        dp[ind+1][2] = dp[ind][2]
        dp[ind+1][3] = dp[ind][3] + dp[ind][2]
    else:
        dp[ind+1][0] = dp[ind][0]*3
        dp[ind+1][1] = dp[ind][1]*3 + dp[ind][0]
        dp[ind+1][2] = dp[ind][2]*3 + dp[ind][1]
        dp[ind+1][3] = dp[ind][3]*3 + dp[ind][2]
        
    dp[ind+1][0]%=MOD
    dp[ind+1][1]%=MOD
    dp[ind+1][2]%=MOD
    dp[ind+1][3]%=MOD

print(dp[-1][3]%MOD)
