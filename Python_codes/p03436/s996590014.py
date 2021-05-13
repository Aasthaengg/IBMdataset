h, w = map(int, input().split())
m = [['#'] * (w+2) for i in range(h+2)]
for j in range(h):
    m[j+1][1:w+1] = list(input()) #適宜変える

white = 0
for i in range(h+2):
    for j in range(w+2):
        if m[i][j] == '.':
            white += 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

seen = [[0] * (w+2) for i in range(h+2)]

todo = [[1, 1]]
seen[1][1] = 1
while(todo != []):
    v = todo.pop(0)
    for i in range(4):
        if m[v[0]+dx[i]][v[1]+dy[i]] != '#' and seen[v[0]+dx[i]][v[1]+dy[i]] == 0:
            seen[v[0]+dx[i]][v[1]+dy[i]] = seen[v[0]][v[1]] + 1
            todo.append([v[0]+dx[i], v[1]+dy[i]])
    
print(white-seen[h][w] if seen[h][w] else -1)