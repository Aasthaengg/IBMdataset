def resolve():
    W, H, M = map(int, input().split())
    x = []
    y = []
    a = []
    a1 = [0]
    a2 = [W]
    a3 = [0]
    a4 = [H]
    for i in range(M):
        X, Y, A = map(int, input().split())
        x.append(X)
        y.append(Y)
        a.append(A)
    for j in range(M):
        if a[j] == 1:
            a1.append(x[j])
        elif a[j] == 2:
            a2.append(x[j])
        elif a[j] == 3:
            a3.append(y[j])
        else:
            a4.append(y[j])
    print((max(min(a4)-max(a3), 0))*(max(min(a2)-max(a1), 0)))
resolve()