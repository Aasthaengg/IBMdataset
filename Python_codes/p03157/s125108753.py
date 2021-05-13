from collections import deque
H,W = map(int,input().split())
grid = [0] * H
for i in range(H):
    grid[i] = input()

ans = 0

done = [[0]*W for _ in range(H)]
for sy in range(H):
    for sx in range(W):
        if done[sy][sx]:
            continue
        # 初期状態
        q = deque()
        q.append([sy,sx])
        done[sy][sx] = 1
        n_white = 0
        n_black = 0
        if grid[sy][sx] == '.':
            n_white += 1
        else:
            n_black += 1

        while q:
            y,x = q.popleft()
            for new_y, new_x in [[y+1,x],[y,x+1],[y-1,x],[y,x-1]]:
                if 0<= new_y < H and 0<= new_x < W and not done[new_y][new_x]:
                    if grid[y][x] != grid[new_y][new_x]:
                        # 色ごとの数更新
                        if grid[new_y][new_x] == '.':
                            n_white += 1
                        else:
                            n_black += 1
                        
                        done[new_y][new_x] = 1
                        q.append([new_y,new_x])
        ans += n_black*n_white
print(ans)