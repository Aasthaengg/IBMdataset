import sys
N, M, Q = map(int, sys.stdin.readline().rstrip().split())

#da[i][j]:(0,0)~(i,j)の長方形の和
def da_generate(h, w, a):
    da = [[0] * w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1, w):
        da[0][i] = da[0][i - 1] + a[0][i]
    for i in range(1, h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i - 1][j] + cnt_w
    return da

#da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和
def da_calc(p, q, x, y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y] - da[x][q - 1]
    if q == 0:
        return da[x][y] - da[p - 1][y]
    return da[x][y] - da[p - 1][y] - da[x][q - 1] + da[p - 1][q - 1]

a = [[0] * N for _ in range(N)]

for _ in range(M):
    l, r = map(int, sys.stdin.readline().rstrip().split())
    a[l - 1][r - 1] += 1

da = da_generate(N, N, a)

for _ in range(Q):
    p, q = map(int, sys.stdin.readline().rstrip().split())
    p -= 1
    q -= 1
    print(da_calc(p, p, q, q))