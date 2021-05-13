def main():
    N,K = map(int,input().split())
    XY = [list(map(int,input().split())) for _ in [0]*N]
    iX = [0]*N
    iY = [0]*N
    for i,xy in enumerate(XY):
        x,y = xy
        iX[i] = x
        iY[i] = y
    iX.sort()
    iY.sort()
    X = {x:i for i,x in enumerate(iX)}
    Y = {y:i for i,y in enumerate(iY)}

    c = [[0]*(N+1) for i in [0]*(N+1)]
    for x,y in XY:
        c[Y[y]+1][X[x]+1] = 1

    for i in range(N):
        ci1 = c[i+1]
        for j in range(N):
            ci1[j+1] += ci1[j]
    for i in range(N):
        c[i+1] = [ci1j+cij for ci1j,cij in zip(c[i+1],c[i])]

    ans = 10**20
    for u in range(N):
        for d in range(u+K-1,N):
            l = 0
            r = K-1
            dY = iY[d]-iY[u]
            cd = c[d+1]
            cu = c[u]
            while r<N:
                if cd[r+1]+cu[l]-cu[r+1]-cd[l] >=K:
                    ans = min(ans, (iX[r] - iX[l])*dY)
                    l+=1
                else:r+=1

    print(ans)
main()