import itertools
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


H, W = list(map(int, sys.stdin.buffer.readline().split()))
S = [sys.stdin.buffer.readline().decode().rstrip() for _ in range(H)]

# 白から黒に来るときだけ+1すればOK
dp = [[INF] * W for _ in range(H)]
dp[0][0] = 1 if S[0][0] == '#' else 0
for h, w in itertools.product(range(H), range(W)):
    for ph, pw in [(h - 1, w), (h, w - 1)]:
        if 0 <= ph < H and 0 <= pw < W:
            d = int(S[ph][pw] == '.' and S[h][w] == '#')
            dp[h][w] = min(dp[h][w], dp[ph][pw] + d)
print(dp[-1][-1])
