import sys
h, w = list(map(int, input().split()))
maze = []
for i in range(h):
    maze.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(h):
    for j in range(w):
        if maze[i][j] == '#':
            flag = False
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and nx < h and ny >= 0 and ny < w and maze[nx][ny] == '#':
                    flag = True
                    break
            if not flag:
                print('No')
                sys.exit()
print('Yes')