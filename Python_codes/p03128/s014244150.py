import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N, M = list(map(int, sys.stdin.buffer.readline().split()))
A = list(map(int, sys.stdin.buffer.readline().split()))

requires = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# dp[i][0]: i 個のマッチ棒を使って作れる整数の最大の桁数
# dp[i][1][-j]: j を何個作るか
dp = [(0, [0] * 9) for _ in range(N + 10)]
for i in range(N):
    d, counts = dp[i]
    if i > 0 and d == 0:
        continue
    for a in A:
        cnts = counts[:]
        cnts[-a] += 1
        dp[i + requires[a]] = max(dp[i + requires[a]], (d + 1, cnts))
ans = ''
for i, cnt in enumerate(dp[N][1]):
    ans += str(9 - i) * cnt
print(ans)
