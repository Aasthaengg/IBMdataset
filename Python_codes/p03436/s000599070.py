from collections import deque

H, W = map(int, input().split())

G = []
black = 0
for i in range(H):
    line = list(input())
    G.append(line)
    black += line.count("#")
    
ls = deque([[0, 0, 0]])
D = [[float("inf")] * W for i in range(H)]
direction = [[1,0], [-1,0], [0,1], [0,-1]]
find = False
while len(ls) > 0:
    h, w, depth = ls.popleft()
    
    if h == H-1 and w == W-1:
        route = depth + 1
        find = True
        break
        
    for dh, dw in direction:
        if h + dh < 0 or H-1 < h + dh: continue
        if w + dw < 0 or W-1 < w + dw: continue
        if depth + 1 < D[h+dh][w+dw] and G[h+dh][w+dw] != "#":
            ls.append([h+dh, w+dw, depth+1])
            D[h+dh][w+dw] = depth + 1
            
if find:
    ans = (H * W) - black - route
    print(ans)
else:
    print(-1)