#%%
H, W = [int(i) for i in input().split()]
maze = [[] for _ in range(H)]

num_black = 0
for i in range(H):
    temp = input()
    for j in temp:
        maze[i].append(j)
        if j == "#":
            num_black += 1
            
#%%
import copy, collections

maze_copy = copy.deepcopy(maze)
color = [["W"] * W for _ in range(H)]


X, Y = 0, 0
vec = [[1, 0], [-1, 0], [0, 1], [0, -1]]
color[Y][X] = "G"
que = collections.deque()
maze_copy[Y][X] = 1
que.append([Y, X])

while len(que) != 0:
    u = que.popleft()
    for y, x in vec:
        temp_x = u[1] + x
        temp_y = u[0] + y
        if (0 <= temp_x < W and 0 <= temp_y < H
                and maze_copy[temp_y][temp_x] == "." and color[temp_y][temp_x] == "W"):
            color[temp_y][temp_x] = "G"
            maze_copy[temp_y][temp_x] = maze_copy[u[0]][u[1]] + 1
            que.append([temp_y, temp_x])
    
if maze_copy[-1][-1] == ".":
    print(-1)
else:
    print(W * H - num_black - maze_copy[-1][-1])

