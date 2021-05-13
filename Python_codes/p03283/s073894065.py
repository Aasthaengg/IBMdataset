N,M,Q = map(int,input().split())
s = [[0 for j in range(501)] for i in range(501)]

for _ in range(M):
    L,R = map(int,input().split())
    s[L][R] += 1

# 二次元累積和
for i in range(1,501):
    for j in range(1,501):
        s[i][j] += s[i-1][j] + s[i][j-1] - s[i-1][j-1]

# クエリに対してO(1)で求める
for _ in range(Q):
    p,q = map(int,input().split())
    print(s[q][q]-s[p-1][q]-s[q][p-1]+s[p-1][p-1])
