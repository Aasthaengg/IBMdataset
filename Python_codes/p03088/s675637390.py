from datetime import datetime as dt
import itertools
N = int(input())
dp = [ [[[0 for _ in range(N + 1) ]for _ in range(5)] for _ in range(5)] for _ in range(5)]

# c1 c2 c3
# 0: dammy (DP を初期化するのにこれがあると便利)
# for c2 in range(4):
#     for c3 in range(4):
#         for c1 in range(4):
#             dp[c3][c2][c1][2] = 1 #末尾2文字に関してDP (規約違反に関しては，
        # 規約違反でない文字列の末尾2文字に対して1文字加えたときに判断できるので)
MOD = 10 ** 9 + 7

dp[0][0][0][0] = 1 # 0→ 存在しない の意味
A = 1
G = 2
C = 3
T = 4

# ~~~~ c1 c2
for i in range(0,N):
    for c1 in range(5): #1文字前
        for c2 in range(5): #2文字前
            for c3 in range(5): # 3文字前
                for c in range(1,5): # 新たな文字を加える
                    if c2 == A and c1 == G and c == C:
                        continue
                    if c3 == A and c2 == G and c == C:
                        continue
                    if c3 == A and c1 == G and c == C:
                        continue
                    if c2 == G and c1 == A and c == C:
                        continue
                    if c2 == A and c1 == C and c == G:
                        continue
                    dp[c2][c1][c][i + 1] +=(dp[c3][c2][c1][i] % MOD)


ans = 0
for c1 in range(1,5):
    for c2 in range(1,5):
        for c3 in range(1,5):
            ans += dp[c3][c2][c1][N]
        # print(f"{alpha[c1] + alpha[c2]}: {dp[c1][c2][N]}")

print(ans % MOD)
