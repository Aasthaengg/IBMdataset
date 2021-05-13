import sys

H, W = map(int, input().split())
G = [list(sys.stdin.readline().strip()) for _ in range(H)]

DP = [[0] * W for _ in range(H)]

DP[0][0] = int(G[0][0] == "#")
for i in range(1, H):
    DP[i][0] = DP[i - 1][0] + int(G[i][0] == "#" and G[i - 1][0] == ".")
for j in range(1, W):
    DP[0][j] = DP[0][j - 1] + int(G[0][j] == "#" and G[0][j - 1] == ".")

for i in range(1, H):
    for j in range(1, W):
        t = int(G[i][j] == "#")
        DP[i][j] = min(DP[i - 1][j] + int(t and G[i - 1][j] == "."), DP[i][j - 1] + int(t and G[i][j - 1] == "."))

print(DP[H - 1][W - 1])
