from collections import deque
def main():
    H, W = map(int,input().split())
    s = [list(map(str,input())) for _ in range(H)]
    dist = [[-1]*W for _ in range(H)]
    
    q = deque([])
    for i in range(H):
        for j in range(W):
            if s[i][j] == "#":
                dist[i][j] = 0
                q.append((i, j))
    
    ans = 0
    while q:
        x, y = q.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < H and 0 <= ny < W and dist[nx][ny] == -1 and s[nx][ny] == '.'):
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                ans = max(ans, dist[nx][ny])
                
    print(ans)

if __name__ == "__main__":
    main()
