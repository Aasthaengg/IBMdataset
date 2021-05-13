from collections import deque


def bfs(y,x):
    global s
    global fl
    global h
    global w
    global ans
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    count = 1
    black = 0
    d = deque()
    # appendするときに計算する
    d.append([y,x])
    fl[y][x] = 1
    if s[y][x]=='#':
        black+=1
    while len(d):
        p = d.pop()
        for k in range(4):
            if 0<=p[1]+dx[k] <w and 0<=p[0]+dy[k] <h and s[p[0]][p[1]]!=s[p[0]+dy[k]][p[1]+dx[k]]:
                if fl[p[0]+dy[k]][p[1]+dx[k]]:
                    continue
                d.append([p[0]+dy[k],p[1]+dx[k]])
                count += 1
                fl[p[0]+dy[k]][p[1]+dx[k]] = 1
                if s[p[0]+dy[k]][p[1]+dx[k]]=='#':
                    black+=1
    ans += black*(count-black)


h, w = map(int, input().split())
s = [input() for i in range(h)]
fl = [[0 for _ in range(w)] for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if not fl[i][j]:
            bfs(i,j)
print(ans)