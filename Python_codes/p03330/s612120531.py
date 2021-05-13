from itertools import permutations, product
INF = float("inf")
N,C=map(int, input().split())
D=[[INF]*(C+1) for _ in range(C+1)]
c = [[-1]*(N+1) for _ in range(N+1)]
for i in range(1, C+1):
    tmp=list(map(int, input().split()))
    for j in range(1, C+1):
        D[i][j] = tmp[j-1]
for i in range(1, N+1):
    tmp=list(map(int, input().split()))
    for j in range(1, N+1):
        c[i][j] = tmp[j-1]
res0 = []
res1 = []
res2 = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if (i+j)%3==0:
            res0.append((i,j))
        elif (i+j)%3==1:
            res1.append((i,j))
        else:
            res2.append((i,j))
ans = INF
dc0 = []
dc1 = []
dc2 = []
for nx in range(1,C+1):
    d0 = 0
    d1 = 0
    d2 = 0
    for i,j in res0:
        d0 += D[c[i][j]][nx]
    for i,j in res1:
        d1 += D[c[i][j]][nx]
    for i,j in res2:
        d2 += D[c[i][j]][nx]
    dc0.append((d0, nx))
    dc1.append((d1, nx))
    dc2.append((d2, nx))
dc0.sort()
dc1.sort()
dc2.sort()

for i, j, k in product(range(0, 3), repeat=3):
    c0 = dc0[i][1]
    c1 = dc1[j][1]
    c2 = dc2[k][1]
    if c0 == c1 or c1 == c2 or c2 == c0:
        continue
    disgust = 0
    for i, j in res0:
        disgust += D[c[i][j]][c0]
    for i, j in res1:
        disgust += D[c[i][j]][c1]
    for i, j in res2:
        disgust += D[c[i][j]][c2]
    ans = min(ans, disgust)
print(ans)