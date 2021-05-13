from itertools import product
MOD = 10**9 + 7
N = int(input())
# XAGC, XGAC, AXGC, AGXC, XACG: prohibited
A=0; C=1; G=2; T=3
cur = [[[1]*4 for j in range(4)] for k in range(4)]
for i in range(4):
    cur[A][G][C] = cur[G][A][C] = cur[A][C][G] = 0

for _ in range(3,N):
    prev = cur
    cur = [[[0]*4 for j in range(4)] for k in range(4)]
    for i, j, k in product(range(4),repeat=3):
        if (j==A and k==G) or (j==G and k==A) or (i==A and k==G) or (i==A and j==G):
            for l in [A,G,T]:
                cur[j][k][l] += prev[i][j][k]
        elif j==A and k==C:
            for l in [A,C,T]:
                cur[j][k][l] += prev[i][j][k]
        else:
            for l in range(4):
                cur[j][k][l] += prev[i][j][k]
    for i, j, k in product(range(4),repeat=3):
        cur[i][j][k] %= MOD

ans = sum(sum(sum(cur[i][j]) for j in range(4)) for i in range(4)) % MOD
print(ans)