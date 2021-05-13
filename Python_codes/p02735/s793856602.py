from collections import deque
h, w = map(int, input().split())
s_list = []
for _ in range(h):
    s = input()
    s_list.append(s)
d = deque()
count = 0
if s_list[0][0] == '#':
    count += 1
d.append([0, 0, count])

vis = [[101 for i in range(w)] for j in range(h)]
if s_list[0][0] == '.':
    vis[0][0] = 0
else:
    vis[0][0] = 1
for x in range(h):
    for y in range(w):
        for xx, yy in [[1, 0], [0, 1]]:
            if (0 <= x + xx < h) & (0 <= y + yy < w):
                if (s_list[x][y] == '.') & (s_list[x + xx][y + yy] == '#'):
                    vis[x + xx][y + yy] = min(vis[x][y] + 1, vis[x + xx][y + yy])
                else:
                    vis[x + xx][y + yy] = min(vis[x][y], vis[x + xx][y + yy])          
print(vis[-1][-1])