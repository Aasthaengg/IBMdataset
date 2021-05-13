S = input()
N = len(S)
ans = 0
MOD = 10**9+7
dp = [[0]*4 for _ in range(2)]
dp[0][0] = 1

for i in range(N):
    if S[i]=='A':
        dp[(i+1)%2][0] = dp[i%2][0]
        dp[(i+1)%2][1] = dp[i%2][0]+dp[i%2][1]
        dp[(i+1)%2][2] = dp[i%2][2]
        dp[(i+1)%2][3] = dp[i%2][3]
    elif S[i]=='B':
        dp[(i+1)%2][0] = dp[i%2][0]
        dp[(i+1)%2][1] = dp[i%2][1]
        dp[(i+1)%2][2] = dp[i%2][1]+dp[i%2][2]
        dp[(i+1)%2][3] = dp[i%2][3]
    elif S[i]=='C':
        dp[(i+1)%2][0] = dp[i%2][0]
        dp[(i+1)%2][1] = dp[i%2][1]
        dp[(i+1)%2][2] = dp[i%2][2]
        dp[(i+1)%2][3] = dp[i%2][2]+dp[i%2][3]
    else:
        dp[(i+1)%2][0] = 3*dp[i%2][0]
        dp[(i+1)%2][1] = dp[i%2][0]+3*dp[i%2][1]
        dp[(i+1)%2][2] = dp[i%2][1]+3*dp[i%2][2]
        dp[(i+1)%2][3] = dp[i%2][2]+3*dp[i%2][3]

    for j in range(4):
        dp[(i+1)%2][j] %= MOD

print(dp[N%2][3])