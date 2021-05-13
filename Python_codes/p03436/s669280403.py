from collections import deque

h, w = map(int, input().split())
Map = [['#'] * (w+2)]
Map += [['#'] + list(input()) + ['#'] for _ in range(h)]
Map += [['#'] * (w+2)]

cnt = 0

for i in range(h+2):
    for j in range(w+2):
        if Map[i][j] == '.':
            cnt += 1
            
stack = deque([(1,1)])
Map[1][1] = 1
moved = [[0,1], [0,-1], [1,0], [-1,0]]

while stack:
    x, y = stack.popleft()
    for s, t in moved:
        if Map[x+s][y+t] == '.':
            stack.append((x+s, y+t))
            Map[x+s][y+t] = Map[x][y] + 1

goal = Map[-2][-2]
if goal == '.':
    print(-1)
else:
    print(cnt - goal)