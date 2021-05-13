from collections import deque
H, W = map(int, input().split())
G = [input() for _ in range(H)]
num = 0
for i in range(H):
    for j in range(W):
        if G[i][j] == ".":
            num += 1
q = deque([(0, 0)])
done = [[-1]*W for _ in range(H)]
done[0][0] = 1
while q:
    w, h = q.popleft()
    for dw, dh in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nw, nh = w+dw, h+dh
        if not (0 <= nw < W and 0 <= nh < H and G[nh][nw] == "." and done[nh][nw] == -1): continue
        done[nh][nw] = done[h][w]+1
        q.append((nw, nh))
if done[H-1][W-1] != -1:
    print(num-done[H-1][W-1])
else:
    print(-1)
