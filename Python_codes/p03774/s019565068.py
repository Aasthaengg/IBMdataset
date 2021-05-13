def dist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])
N,M = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
Y = [list(map(int,input().split())) for _ in range(M)]
for i in range(N):
    dmin = 10**9
    for j in range(M-1,-1,-1):
        d = dist(X[i],Y[j])
        if d<=dmin:
            dmin = d
            ind = j+1
    print(ind)