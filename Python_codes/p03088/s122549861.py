import sys
input = sys.stdin.readline

n = int(input())

dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
c = [0, 1, 2, 3]
import itertools
pers = itertools.product(c, repeat=3)
for p in pers:
    if p in [(0, 1, 2), (0, 2, 1), (1, 0, 2)]:
        continue
    dp[3][p[0]][p[1]][p[2]] = 1
for i in range(4, n + 1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if (j, k, l) in [(0, 1, 2), (0, 2, 1), (1, 0, 2)]:
                    continue
                elif (j == 0 and l == 1) or (j == 0 and k == 1):
                    dp[i][j][k][l] = sum([dp[i - 1][k][l][x] for x in range(4) if x != 2])
                else:
                    dp[i][j][k][l] = sum([dp[i - 1][k][l][x] for x in range(4)])
ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[-1][j][k][l]
print(ans % (10**9 + 7))