h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

x = [[-1] for _ in range(h*w+d+1)]
m = []
for i in range(h):
    for j in range(w):
        x[a[i][j]] = [i, j]
        m.append([a[i][j], i, j])
m.sort()
visit = [[-1 for _i in range(w)] for _j in range(h)]

for pos, xx, yy in m:
    if visit[xx][yy] < 0:
        visit[xx][yy] = 0
        while x[pos+d][0] >= 0:
            g, h = x[pos+d]
            visit[g][h] = visit[xx][yy] + abs(g-xx)+abs(h-yy)
            xx = g
            yy = h
            pos = a[xx][yy]
for l, r in lr:
    print(visit[x[r][0]][x[r][1]]-visit[x[l][0]][x[l][1]])