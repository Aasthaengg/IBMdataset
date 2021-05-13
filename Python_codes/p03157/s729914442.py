import sys
sys.setrecursionlimit(10 ** 9)
H, W = map(int, input().split())
G = [list(input()) for i in range(H)]
C = [[0] * W for i in range(H)]


def dfs(nh, nw, color):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    C[nh][nw] = color
    for dh, dw in direction:
        if not ((0 <= nh + dh < H) and (0 <= nw + dw < W)):
            continue
        if C[nh + dh][nw + dw] != 0:
            continue
        if G[nh][nw] == G[nh + dh][nw + dw]:
            continue
        C[nh + dh][nw + dw] = color
        dfs(nh + dh, nw + dw, -color)


Color = 1
for h in range(H):
    for w in range(W):
        if C[h][w] == 0:
            dfs(h, w, Color)
            Color += 1


Count = {}
for h in range(H):
    for w in range(W):
        Count[C[h][w]] = 0
        Count[-C[h][w]] = 0


for h in range(H):
    for w in range(W):
        Count[C[h][w]] += 1


ans = 0
for key in Count.keys():
    ans += Count[key] * Count[-key]

print(ans // 2)
