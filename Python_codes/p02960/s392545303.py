S = list(input())
l = len(S)
mod = 10**9+7

A = []
a = 1
for i in range(l):
    A.append(a)
    a = (10*a) % 13

A.reverse()

dp = [[0]*13 for i in range(l)]

for i in range(l):
    for j in range(13):
        if i == 0:
            if S[i] != '?':
                dp[i][(int(S[i])*A[i]) % 13] = 1
            else:
                for k in range(10):
                    dp[i][(k*A[i]) % 13] = 1
        else:
            if S[i] != '?':
                dp[i][j] = dp[i-1][(j-int(S[i])*A[i]) % 13]
            else:
                for k in range(10):
                    dp[i][j] += dp[i-1][(j-k*A[i]) % 13]
                    dp[i][j] = (dp[i][j]) % mod
print(dp[l-1][5])