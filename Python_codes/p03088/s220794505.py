from itertools import product
N = int(input())
MOD = 10**9+7
D = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+3)]
D[0][3][3][3] = 1
for n in range(1,N+1):
    for i, j, k, l in product(range(4), repeat=4):
        if (i,j,l)==(2,1,0) or (i,k,l) == (2,1,0) or (i,j,k) == (1,2,0) or (i,j,k) == (2,0,1) or (i,j,k) == (2,1,0): continue
        D[n][i][j][k] += D[n-1][j][k][l]%MOD
res = 0
for i, j, k in product(range(4),repeat=3):
    res += D[N][i][j][k]
    res %= MOD
print(res)