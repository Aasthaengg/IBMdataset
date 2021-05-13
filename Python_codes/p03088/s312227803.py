import sys
input = sys.stdin.readline

n = int(input())

dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
c = [0, 1, 2, 3]
import itertools
pers = itertools.product(c, repeat=3)
ng_3 = [(0, 1, 2), (0, 2, 1), (1, 0, 2)]
for p in pers:
    if p in ng_3:
        continue
    dp[3][p[0]][p[1]][p[2]] = 1
for i in range(3, n):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    if (m, j, k) in ng_3 or (m == 0 and k == 1 and l == 2) or (m == 0 and j == 1 and l == 2):
                        continue
                    dp[i + 1][m][j][k] += dp[i][j][k][l]
ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[-1][j][k][l]
print(ans % (10**9 + 7))