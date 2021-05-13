n = int(input())
if n == 3:
    print(61)
    exit()
MOD = 10 ** 9 + 7
# dp[i][i-1][i-2][i-3][i-4]
dp = [[[[[0] * (4) for _ in range(4)] for i in range(4)] for i in range(4)] for i in range(n + 1)]

to = {0:"A", 1:"C", 2:"G", 3:"T"}
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            for i4 in range(4):
                if "AGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue
                if "ACG" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "GAC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "AAGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "ACGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "AGGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "ATGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "AGAC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "AGCC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "AGGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                if "AGTC" in to[i1] + to[i2] + to[i3] + to[i4]:
                    continue 
                dp[4][i1][i2][i3][i4] = 1

for i in range(4, n):
    for i1 in range(4):
        for i2 in range(4):
            for i3 in range(4):
                for i4 in range(4):
                    if "AGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue
                    if "ACG" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "GAC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "AAGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "ACGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "AGGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "ATGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "AGAC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "AGCC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "AGGC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    if "AGTC" in to[i1] + to[i2] + to[i3] + to[i4]:
                        continue 
                    for j in range(4):
                        dp[i + 1][i1][i2][i3][i4] += dp[i][i2][i3][i4][j]
                        dp[i + 1][i1][i2][i3][i4] %= MOD

ans = 0
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            for i4 in range(4):
                ans += dp[-1][i1][i2][i3][i4]
                ans %= MOD
print(ans % MOD)