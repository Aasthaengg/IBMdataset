H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

visited = [[False] * W for _ in range(H)]

def search(sx, sy) :
    q = [(sx, sy)]
    visited[sy][sx] = True
    
    b, w = 0, 0
    if S[sy][sx] == '#' :
        b += 1
    else :
        w += 1
        
    while q :
        cx, cy = q.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) :
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < W and 0 <= ny < H and not visited[ny][nx] and S[cy][cx] != S[ny][nx] :
                visited[ny][nx] = True
                q.append((nx, ny))
                if S[ny][nx] == '#' :
                    b += 1
                else :
                    w += 1           
    return b * w

ret = 0
for y in range(H) :
    for x in range(W) :
        if not visited[y][x] :
            ret += search(x, y)
            
print(ret)