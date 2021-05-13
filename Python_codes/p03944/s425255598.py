w,h,n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]
X = [0,w]
Y = [0,h]
for x,y,a in xya:
    if a == 1:
        X[0] = max(X[0], x)
    elif a == 2:
        X[1] = min(X[1], x)
    elif a == 3:
        Y[0] = max(Y[0], y)
    else:
        Y[1] = min(Y[1], y)
if X[0] >= X[1] or Y[0] >= Y[1]: print(0)
else: print(abs(X[0]-X[1])*abs(Y[0]-Y[1]))