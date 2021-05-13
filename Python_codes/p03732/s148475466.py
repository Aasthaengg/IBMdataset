N, W = map(int, input().split())
app = [list(map(int, input().split())) for i in range(N)]

data = [[] for i in range(4)]

for w, v in app:
    if w == app[0][0]:
        data[0].append(v)
    elif w == app[0][0] + 1:
        data[1].append(v)
    elif w == app[0][0] + 2:
        data[2].append(v)
    elif w == app[0][0] + 3:
        data[3].append(v)

for i in range(4):
    data[i].sort(reverse=True)

for i in range(4):
    for j in range(len(data[i])-1):
        data[i][j+1] += data[i][j]

for i in range(4):
    data[i].append(0)
    data[i].sort()

ans = 0
for a in range(len(data[0])):
    for b in range(len(data[1])):
        for c in range(len(data[2])):
            for d in range(len(data[3])):
                if a * app[0][0] + b * (app[0][0]+1) + c * (app[0][0]+2) + d * (app[0][0]+3) <= W:
                    ans = max(ans, data[0][a] + data[1][b] + data[2][c] + data[3][d])

print(ans)