N,K = map(int,input().split())
x = [0]*N
y = [0]*N
for i in range(N):
    x[i], y[i] = map(int,input().split())

ans = float('inf')
sx = sorted(x)
sy = sorted(y)
for xi in range(N):
    for xj in range(xi+1,N):
        for yi in range(N):
            for yj in range(yi+1,N):
                lx = sx[xi]
                rx = sx[xj]
                by = sy[yi]
                uy = sy[yj]
                cnt = 0
                for i in range(N):
                    if lx <= x[i] <= rx and by <= y[i] <= uy:
                        cnt += 1
                if cnt >= K:
                    area = (rx-lx)*(uy-by)
                    ans = min(ans,area)
print(ans)