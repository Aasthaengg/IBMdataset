N, M = map(int, input().split())

x = [[] for _ in range(N)]
a = [None] * M
for i in range(M):
    P, Y = map(int, input().split())
    x[P-1].append(Y)
    a[i] = (P, Y)

y = {}
for i in range(N):
    x[i].sort()
    for j, Y in enumerate(x[i]):
        y[(i+1, Y)] = j + 1
for i in range(M):
    print('{}{}'.format(str(a[i][0]).zfill(6), str(y[a[i]]).zfill(6)))
