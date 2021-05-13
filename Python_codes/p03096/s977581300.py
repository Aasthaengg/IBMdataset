N = int(input())
C = [0 for i in range(N)]

for i in range(N):
    C[i] = int(input())

sosu = 10 ** 9 + 7

dp = [1 for i in range(N)]
alpha = {}
alpha[C[0]] = [0]
mae = C[0]
for i in range(1,N):
    dp[i] = dp[i-1]
    if C[i] != mae:
        if C[i] in alpha.keys():
            length = len(alpha[C[i]])
            lastnum = alpha[C[i]][length - 1]
            dp[i] += dp[lastnum]
            alpha[C[i]].append(i)
        else:
            alpha[C[i]] = [i]
    mae = C[i]
    dp[i] = dp[i] % sosu
print(dp[N-1])
