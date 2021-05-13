S = input()
s = 'ABC'
N = len(S)
C = 10**9+7
dp = [[0]*4 for _ in range(N+1)]
dp[N][3] = 1
for i in reversed(range(N)):
    for j in range(3):
        if i < j:
            continue
        dp[i][j] = ((1+(S[i] == '?')*2)*dp[i+1][j] +
                    (S[i] in {s[j], '?'})*dp[i+1][j+1]) % C
    if i>=3:
        dp[i][3] = ((1+(S[i] == '?')*2)*dp[i+1][3]) % C
print(dp[0][0])