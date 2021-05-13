def resolve():
    x = []
    y = []
    c = []
    ans = []
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for _ in range(M):
        X, Y, C = map(int, input().split())
        x.append(X)
        y.append(Y)
        c.append(C)
    ans.append(min(a)+min(b))
    for i in range(M):
        ans.append(a[x[i]-1]+b[y[i]-1]-c[i])
    print(min(ans))
resolve()