N = int(input())
XY = []
for i in range(N):
    XY.append(list(map(int,input().split())))

if N!=1:
    pqs = []
    for i in range(N):
        for j in range(i+1,N):
            X1 = XY[i][0]
            Y1 = XY[i][1]
            X2 = XY[j][0]
            Y2 = XY[j][1]
            pqs.append(str(X1-X2)+","+str(Y1-Y2))
            pqs.append(str(X2-X1)+","+str(Y2-Y1))

    from collections import Counter
    C = dict(Counter(pqs))
    out = N - max(C.values())
    print(out)
else:
    print(1)