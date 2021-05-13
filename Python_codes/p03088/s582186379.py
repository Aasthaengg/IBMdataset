N = int(input())
MOD = 10**9+7

dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
A,G,C,T = 0,1,2,3
for i in range(4):
    for j in range(4):
        for k in range(4):
            if (i,j,k) in [(A,G,C), (A,C,G), (G,A,C)]: continue
            dp[i][j][k] = 1

for _ in range(N-3):
    dp2 = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i,j,k) in [(A,G,C), (A,C,G), (G,A,C)]: continue
                for l in range(4):
                    if (j,k,l) in [(A,G,C), (A,C,G), (G,A,C)]: continue
                    if (i,k,l) == (A,G,C) or (i,j,l) == (A,G,C): continue
                    dp2[j][k][l] += dp[i][j][k]
                    dp2[j][k][l] %= MOD
    dp = dp2

ans = 0
for row in dp:
    for row2 in row:
        ans += sum(row2)
print(ans%MOD)