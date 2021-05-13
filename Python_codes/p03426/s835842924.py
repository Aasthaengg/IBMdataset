import sys;input=sys.stdin.readline
H, W, D = map(int, input().split())
def dist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])
X = []
for _ in range(H):
    X.append(list(map(int, input().split())))

d = dict()
for i in range(H):
    x = X[i]
    for j in range(W):
        d[x[j]] = (i, j)
Ls = []
for i in range(1, D+1):
    tmp = [0]
    st = d[i]
    j = i
    while j in d:
        tmp.append(tmp[-1]+dist(st, d[j]))
        st = d[j]
        j += D
    Ls.append(tmp)

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    a, b = divmod(x, D)
    c, d = divmod(y, D)
    if b > 0:
        print(Ls[b-1][c+1]-Ls[b-1][a+1])
    else:
        print(Ls[b-1][c]-Ls[b-1][a])
