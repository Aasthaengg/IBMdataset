N, K = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(N)]
xy.sort(key=lambda t: t[0])
ans = 10**20

for i in range(N):
    for j in range(i+K-1, N):
        xlen = xy[j][0]-xy[i][0]
        ys = []
        
        for k in range(i, j+1):
            ys.append(xy[k][1])
            
        ys.sort()
        ylen = 10**20
        
        for k in range(len(ys)-K+1):
            ylen = min(ylen, ys[k+K-1]-ys[k])
        
        ans = min(ans, xlen*ylen)
    
print(ans)