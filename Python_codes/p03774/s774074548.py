def dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])
N,M = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
Y = [list(map(int,input().split())) for _ in range(M)]
for i in range(N):
    x,y = X[i]
    ind = M+1
    dmin = 10**9
    for j in range(M):
        c,d = Y[j]
        d = dist((x,y),(c,d))
        if d<dmin:
            ind = j+1
            dmin = d
    print(ind)