from operator import itemgetter

n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    x, y, z = info[i]
    info[i].append(-x-y-z)
    info[i].append(-x-y+z)
    info[i].append(-x+y-z)
    info[i].append(-x+y+z)
    info[i].append(+x-y+z)
    info[i].append(+x+y-z)
    info[i].append(+x-y-z)
    info[i].append(+x+y+z)

ans = 0
for i in range(8):
    info = sorted(info, key=itemgetter(i + 3), reverse=True)
    x, y, z = 0, 0, 0
    for j in range(m):
        x += info[j][0]
        y += info[j][1]
        z += info[j][2]
    res = abs(x) + abs(y) + abs(z)
    ans = max(res, ans)
print(ans)
