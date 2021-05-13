"""
解法１：
startとgoalの組み合わせの全探索で調べる。
マス目の数は最大で400なので、組み合わせの数は最大で約160000.
各組み合わせごとにBFSで最短経路を調べるので、400回ループが必要。
なので計算時間としてはO(H^3W^3)

解法２：
ワーシャルフロイドで各ノードから各ノードへの最短経路を求める。
計算量としては、O(H^3W^3となる)。

解法１だとなんかTLEするので、解法２で行く。
"""

H,W = map(int,input().split())
MAP = [list(input()) for _ in range(H)]
dp = [[float("INF")]*(H*W) for _ in range(H*W)]
adjecents = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(H):
    for j in range(W):
        if MAP[i][j] == ".":
            pointer = i*W + j
            dp[pointer][pointer] = 0
            for a,b in adjecents:
                x = i + a
                y = j + b
                if 0<=x<H and 0<=y<W and MAP[x][y] == ".":
                    pointer2 = x*W + y
                    dp[pointer][pointer2] = 1

for i in range(H*W):
    for j in range(H*W):
        for k in range(H*W):
            dp[j][k] = min(dp[j][k],dp[j][i]+dp[i][k])

ans = 0
for i in range(H*W):
    for j in range(H*W):
        if dp[i][j] != float("INF"):
            ans = max(ans,dp[i][j])
print(ans)
