MOD = pow(10,9)+7
S = input()[::-1]
N = len(S)

DP = [[0]*13 for i in range(N)]
K = 1
for i in range(N):
    if S[i]=="?":
        for j in range(10):
            if i==0:
                DP[0][(j*K)%13] = 1
            else:
                for k in range(13):
                    DP[i][(j*K+k)%13] += DP[i-1][k]
    else:
        j = int(S[i])*K
        if i==0:
            DP[0][(j*K)%13] = 1
        else:
            for k in range(13):
                DP[i][(j+k)%13] += DP[i-1][k]
    K = (K*10)%13
    for j in range(13):
        DP[i][j] = DP[i][j]%MOD
print(DP[N-1][5]%MOD)