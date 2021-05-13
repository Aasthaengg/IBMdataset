def resolve():
    N, K = list(map(int, input().split()))
    XY = []
    X = []
    Y = []
    for _ in range(N):
        x, y = list(map(int, input().split()))
        XY.append((x, y))
        X.append(x)
        Y.append(y)
    
    X.sort()
    Y.sort()
    
    ans = float("inf")
    for i in range(N-1):
        for j in range(i+1, N):
            for k in range(N-1):
                for l in range(k+1, N):
                    cnt = 0
                    xmin, xmax, ymin, ymax = X[i], X[j], Y[k], Y[l]
                    for x, y in XY:
                        if xmin <= x <= xmax and ymin <= y <= ymax:
                            cnt += 1
                    if cnt >= K:
                        ans = min(ans, abs(xmax-xmin)*abs(ymax-ymin))
    print(ans)




if '__main__' == __name__:
    resolve()