"""
T:0
A:1
C:2
G:3
"""

N = int(input())

dp = [[[[0]*4 for b in range(4)] for a in range(4)] for i in range(N+1)]
dp[0][0][0][0] = 1

for i in range(N):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    if b == 1 and c == 3 and d == 2: # AGC
                        continue
                    if b == 1 and c == 2 and d == 3: # ACG
                        continue
                    if b == 3 and c == 1 and d == 2: # GAC
                        continue
                    if N <= 3:
                        dp[i+1][b][c][d] = 1
                        continue
                    if a == 1 and b == 3 and d == 2: # AGXC
                        continue
                    if a == 1 and c == 3 and d == 2: # AXGC
                        continue
                    dp[i+1][b][c][d] += dp[i][a][b][c]
                    dp[i+1][b][c][d] %= ((10**9)+7)

ans = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            ans += dp[N][a][b][c]
            ans %= ((10**9)+7)

print(ans)