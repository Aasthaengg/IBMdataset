import sys
h, w = map(int, input().split())
C = [list(input()) for i in range(h)]
ans = 0

for i in range(h):
    for j in range(w):
        visited = [[0 for i in range(w)] for i in range(h)]
        data = []
        if C[i][j] == '.':
            data.append([i, j])
            visited[i][j] = 1
            
            dy_dx = [[1,0], [0,1], [-1,0], [0,-1]]
            
            while len(data) > 0:
                now = data.pop(0)
                for k in range(4):
                    y = now[0] + dy_dx[k][0]
                    x = now[1] + dy_dx[k][1]
                    
                    if 0 <= y and y < h and 0 <= x and x < w:
                        if C[y][x] != '#' and visited[y][x] == 0:
                            #移動回数カウント
                            visited[y][x] = visited[now[0]][now[1]] + 1
                            data.append([y, x])
        for l in range(h):
            for m in range(w):
                ans = max(ans, visited[l][m])

print(ans - 1)