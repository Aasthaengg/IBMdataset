n,k = map(int,input().split())
X = [0]*n
Y = [0]*n
for i in range(n):
    X[i],Y[i] = map(int,input().split())

Xs = sorted(X)
Ys = sorted(Y)
XY = sorted(list(zip(X,Y)))
ans = 1e100
for i in range(n-k+1):
    for j in range(i+k-1,n):
        w = Xs[j] - Xs[i]
        XYs = sorted(XY[i:j+1],key = lambda x:x[1])
        h = 1e100
        for l in range(len(XYs) - k + 1):
            h = min(h, XYs[l + k - 1][1] - XYs[l][1])
        ans = min(ans , h*w)
print(ans)
