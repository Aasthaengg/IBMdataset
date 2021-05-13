N = int(input())
MOD = 10**9 + 7

# DP[n][a][b][c] := n-2文字目がa, n-1文字目がb, n文字目がcであるような長さnの文字列の数
DP = [[[[0 for _ in range(4)] for _ in range(4)]
       for _ in range(4)] for _ in range(N + 1)]

# T=0, A=1, G=2, C=3　とする

# DP初期化（3文字）
# AGC(123), GAC(213), ACG(132)を除外
for a in range(4):
    for b in range(4):
        for c in range(4):
            if (a, b, c) not in ((1, 2, 3), (2, 1, 3), (1, 3, 2)):
                DP[3][a][b][c] = 1

# 4~N文字の文字列について
# AGC(123), GAC(213), ACG(132)に加え、A*GC(1*23), AG*C(12*3)も除外
for i in range(4, N + 1):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                # 末尾が T or A の場合は特に制限はない
                DP[i][b][c][0] += DP[i - 1][a][b][c]
                DP[i][b][c][1] += DP[i - 1][a][b][c]
                # 末尾が G の場合、ACGになってはならない
                if (b, c) != (1, 3):
                    DP[i][b][c][2] += DP[i - 1][a][b][c]
                # 末尾がCの場合、AGC, GAC, A*GC, AG*Cは不適
                if (b, c) != (1, 2) and (b, c) != (2, 1) and (a, c) != (1, 2) and (a, b) != (1, 2):
                    DP[i][b][c][3] += DP[i - 1][a][b][c]

ans = 0
# 末尾3文字（計64通り）の総和
for a in range(4):
    for b in range(4):
        for c in range(4):
            ans += DP[N][a][b][c]
            ans %= MOD

print(ans % MOD)
