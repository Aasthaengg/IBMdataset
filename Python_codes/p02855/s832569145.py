from collections import deque
H,W,K = map(int,input().split())
Map = [[0] * W for _ in range(H)]
for i in range(H):
    s = input()
    for j in range(W):
        Map[i][j] = s[j]

ans = [[0] * W for _ in range(H)]

now_count = 1

for y in range(H):
    q = deque()
    for x in range(W):
        q.append([y,x])
        if Map[y][x] == '#':
            while q:
                _y,_x = q.pop()
                ans[_y][_x] = now_count
            now_count += 1
    if q:
        if len(q) == W and y > 0:
            ans[y] = ans[y-1]
        elif len(q) < W:
            while q:
                _y,_x = q.pop()
                ans[_y][_x] = now_count - 1
for y in range(-1,-H-1,-1):
    if ans[y] == [0] * W:
        ans[y] = ans[y+1]
for y in range(H):
    ans[y] = list(map(str,ans[y]))
    print(' '.join(ans[y]))

