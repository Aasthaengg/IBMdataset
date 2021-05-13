n,k = map(int, input().split())
xs = []
ys = []
ps = []
for i in range(n):
    x,y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    ps.append((x,y))
# 座圧
xs = sorted(list(set(xs)))
ys = sorted(list(set(ys)))
xdic = {x:i for i, x in enumerate(xs)}
ydic = {y:i for i, y in enumerate(ys)}
xrdic = {i:x for i, x in enumerate(xs)}
yrdic = {i:y for i, y in enumerate(ys)}
nx = len(xs)
ny = len(ys)


fs = [[0] * (1+ny) for i in range(nx+1)]
for x,y in ps:
    ix = xdic[x]
    iy = ydic[y]
    fs[ix][iy] += 1

acc = [[0] * (1+ny) for i in range(nx+1)]
for i in range(nx):
    for j in range(ny):
        acc[i+1][j+1] = acc[i+1][j] + acc[i][j+1] - acc[i][j] + fs[i][j]

def calc(sx,sy,tx,ty):
    ix1 = xrdic[sx]
    ix2 = xrdic[tx]
    iy1 = yrdic[sy]
    iy2 = yrdic[ty]
    return (ix2-ix1) * (iy2-iy1)

# print(xs,xdic,".",ys,ydic)
ans = 10**20
for sx in range(nx+1):
    for sy in range(ny+1):
        for tx in range(sx+1, nx+1):
            for ty in range(sy+1, ny+1):
                cnt = acc[tx][ty] - acc[sx][ty] - acc[tx][sy] + acc[sx][sy]
                if cnt >= k:
                    S = calc(sx,sy,tx-1,ty-1)
                    ans = min(ans, S)
print(ans)