h, w, k = map(int,input().split())
maze = []
res = []
for _ in range(h):
    l = list(input())
    maze.append(l)
    res.append([None] * w)
wrote = False
colornum = 0
for i in range(h):
    if maze[i].count("#") == 0:
        if wrote is False:
            continue
        else:
            for j in range(w):
                res[i][j] = res[i-1][j]
            continue
    wrote = True
    colornum += 1
    passFirst = False
    for j in range(w):
        if maze[i][j] == "#":
            if passFirst is True:
                colornum += 1
                res[i][j] = colornum
            else:
                res[i][j] = colornum
                passFirst = True
        else:
            res[i][j] = colornum

from pprint import pprint

for i in range(1, h):
    if res[h-1-i].count(None) == w:
        for j in range(w):
            res[h-1-i][j] = res[h-1-i+1][j]

if res[h-1].count(None) == w:
    for j in range(w):
        res[h-1][j] = res[h-2][j]


for i in range(h):
    print(" ".join(list(map(str, res[i]))))
