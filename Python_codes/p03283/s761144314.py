N, M, Q = list(map(int,input().split()))
L = []
R = []
for i in range(M):
    in1, in2 = map(int,input().split())
    L.append(in1 - 1)
    R.append(in2 - 1)
p = []
q = []
for i in range(Q):
    in1, in2 = map(int,input().split())
    p.append(in1 - 1)
    q.append(in2 - 1)
    
a = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    a[L[i]][R[i]] += 1
    
def d2_add(a):
    w = len(a[0])
    h = len(a)
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

def d2_calc(da, p, q, x, y):
    if p > x or q > y:  return 0
    if p == 0 and q == 0:  return da[x][y]
    if p == 0:  return da[x][y] - da[x][q - 1]
    if q == 0:  return da[x][y] - da[p - 1][y]
    return da[x][y] - da[p - 1][y] - da[x][q - 1] + da[p - 1][q - 1]

ret = d2_add(a)
for i in range(Q):
    ans = d2_calc(ret, p[i], p[i], q[i], q[i])
    print(ans)