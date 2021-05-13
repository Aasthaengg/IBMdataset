N,K = map(int,input().split())
XY = [list(map(int,input().split())) for _ in [0]*N]

iX = sorted(x for x,y in XY)
iY = sorted(y for x,y in XY)
X = {x:i for i,x in enumerate(iX)}
Y = {y:i for i,y in enumerate(iY)}

c = [[0]*(N+1) for i in [0]*(N+1)]
for x,y in XY:
    c[Y[y]+1][X[x]+1] = 1

for i in range(N):
    for j in range(N):
        c[i+1][j+1] += c[i+1][j]
for i in range(N):
    for j in range(N):
        c[i+1][j+1] += c[i][j+1]

ans = 10**20
for l in range(N):
    for r in range(l+1,N):
        u = 0
        d = 1
        dX = iX[r] - iX[l]
        while d<N:
            if c[d+1][r+1]+c[u][l]-c[u][r+1]-c[d+1][l] >=K:
                ans = min(ans, dX*(iY[d]-iY[u]))
                u+=1
            else:d+=1

print(ans)