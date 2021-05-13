N, M, Q = map(int, input().split())

X = [[0]*N for _ in range(N)] 
for _ in range(M):
    l, r = map(int, input().split())
    X[l-1][r-1] += 1

for i in range(N):
    for j in range(1,N):
        X[i][j] += X[i][j-1]

ans = []
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    num = 0
    for k in range(p, q+1):
        knum = X[k][q] - X[k][p-1] if p>=1 else X[k][q]
        num += knum
    ans.append(num)

print('\n'.join(map(str, ans)))