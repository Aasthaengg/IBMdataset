from collections import *
import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
mas = []
for i in range(H):
    line = input()
    temp = []
    for j in range(W):
        temp.append(line[j])
    mas.append(temp)

color = []
for i in range(H):
    color.append([-1] * W)

def DFS(node, c_color):
    x = node[0]
    y = node[1]
    nb = [[x, y-1], [x, y+1], [x+1, y], [x-1, y]]
    deq = deque()
    for i in range(4):
        if(nb[i][0] >= 0 and nb[i][0] < H and nb[i][1] >= 0 and nb[i][1] < W):
            if(color[nb[i][0]][nb[i][1]] == -1):
                deq.append(nb[i])

    deq_ = deque()
    while(deq):
        next_node = deq.popleft()
        if(mas[next_node[0]][next_node[1]] != mas[node[0]][node[1]]):
            color[next_node[0]][next_node[1]] = c_color
            deq_.append(next_node)
            
    while(deq_):
        next_node = deq_.popleft()
        DFS(next_node, c_color)
    return
        
current_color = 0
for i in range(H):
    for j in range(W):
        if(color[i][j] >= 0):
            continue
        else:
            color[i][j] = current_color
            DFS([i, j], current_color)
            current_color += 1

color_num = []
for i in range(current_color):
    color_num.append([0, 0])


for i in range(H):
    for j in range(W):
        if(mas[i][j] == '#'):
            color_num[color[i][j]][0] += 1
        else:
            color_num[color[i][j]][1] += 1

ans = 0
for i in range(len(color_num)):
    ans += color_num[i][0] * color_num[i][1]

print(ans)
