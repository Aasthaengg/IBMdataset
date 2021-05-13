p = 10**9+7
S = input().strip()
A = [[0 for k in range(13)] for j in range(13)]
for j in range(13):
    for k in range(13):
        for m in range(10):
            if (10*k+m)%13==j:
                A[j][k] = 1
                break
B = [[0 for _ in range(10)] for _ in range(13)]
for j in range(13):
    for m in range(10):
        for k in range(13):
            if (10*k+m)%13==j:
                B[j][m] = k
                break
N = len(S)
dp = [[0 for _ in range(13)] for _ in range(N+1)]
for j in range(13):
    if S[0]!="?":
        dp[1][j] = int(int(S[0])==j)
    else:
        if j<10:
            dp[1][j] = 1
for i in range(2,N+1):
    for j in range(13):
        if S[i-1]!="?":
            dp[i][j] = (dp[i][j]+dp[i-1][B[j][int(S[i-1])]])%p
        else:
            for k in range(13):
                dp[i][j] = (dp[i][j]+dp[i-1][k]*A[j][k])%p
print(dp[N][5])