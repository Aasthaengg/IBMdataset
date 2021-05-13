import os
import sys
from collections import defaultdict

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N, W = list(map(int, sys.stdin.readline().split()))
WV = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp[w]: w 以下で選ぶときの最大の価値
dp = defaultdict(int)
dp[0] = 0
for w, v in WV:
    for k, d in list(dp.items()):
        dp[k + w] = max(dp[k + w], d + v)

ans = 0
for w, v in dp.items():
    if w <= W:
        ans = max(ans, v)
print(ans)
