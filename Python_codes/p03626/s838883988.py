N = int(input())
S = ["0"+input() for _ in range(2)]

mod = 10**9 + 7
dp = [0]*(N+1)

if S[0][1] == S[1][1]:
    dp[1] = 3
    i = 1
else:
    dp[1] = 6
    dp[2] = 6
    i = 2

while i <= N-1:
    if S[0][i] == S[1][i]:#pattern1
        if S[0][i+1] == S[1][i+1]:
            dp[i+1] = (dp[i]*2)%mod
            i += 1
        else:
            dp[i+1] = (dp[i]*2) %mod
            dp[i+2] = dp[i+1]
            i += 2
    else:
        if S[0][i+1] == S[1][i+1]:
            dp[i+1] = dp[i]
            i += 1
        else:
            dp[i+1] = (dp[i]*3)%mod
            dp[i+2] = dp[i+1]
            i += 2

print(dp[N])        
