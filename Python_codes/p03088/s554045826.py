N = int(input())
dp = [[[[0 for _ in range(4) ]for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
MOD = 10 ** 9 + 7

dp[0][0][0][0] = 1 
A, G, C, T = 0, 1, 2, 3

for i in range(N):
    for c1 in range(4): 
        for c2 in range(4): 
            for c3 in range(4): 
                for c in range(4): 
                    if (c, c1, c2) in [(A,G,C), (G,A,C), (A,C,G)]:
                        continue
                    if (c, c2, c3) == (A,G,C):
                        continue
                    if (c, c1, c3) == (A,G,C):
                        continue
                    dp[i+1][c][c1][c2] += (dp[i][c1][c2][c3] % MOD)

ans = 0
for c1 in range(4):
    for c2 in range(4):
        for c3 in range(4):
            ans += dp[N][c3][c2][c1]

print(ans % MOD)
