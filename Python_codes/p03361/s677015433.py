import numpy as np

H,W = [int(i) for i in input().split()]

maze = [['.']*(W+2)]
for i in range(H):
    maze.append(list('.'+input()+'.'))
maze.append(['.']*(W+2))

for i in range(1,H+1):
    for j in range(1,W+1):
        if maze[i][j] == '#':
            if maze[i-1][j] != '#' and maze[i+1][j] != '#' and maze[i][j-1] != '#' and maze[i][j+1] != '#':
                print('No')
                exit()

print('Yes')
