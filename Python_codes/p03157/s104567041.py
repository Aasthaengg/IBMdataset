import sys
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
F = [list(input()) for _ in range(H)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
seen = [[0] * W for _ in range(H)]

# Fの点を頂点とするグラフを考える。グラフの連結成分に'#'がbコ, '.'がwコある場合、
# b*wが条件を満たす

def dfs(sy, sx):
    seen[sy][sx] = 1
    b, w = 1, 0
    
    for dy, dx in move:
      ny = sy + dy
      nx = sx + dx
      if 0 <= ny < H and 0 <= nx < W and F[ny][nx] != F[sy][sx] and not seen[ny][nx]:
        p = dfs(ny, nx)
        b += p[1]  # 逆にしている
        w += p[0]  # 天才か？
    return (b, w)
        
count = 0
for i in range(H):
    for j in range(W):
        if not seen[i][j]:
            b, w = dfs(i, j)
            count += b * w

print(count)