N,C=map(int, input().split())
D=[list(map(int, input().split())) for _ in range(C)]
c=[list(map(int, input().split())) for _ in range(N)]

from collections import Counter
t=[Counter([c[i][j] for i in range(N) for j in range(N) if (i+j)%3==m]) for m in range(3)]

ans = 10**9
for i in range(C):
    for j in range(C):
        if i==j: continue
        for k in range(C):
            if i==k or j==k: continue
            d = 0
            for before in range(C):
                d += D[before][i] * t[0][before+1]
                d += D[before][j] * t[1][before+1]
                d += D[before][k] * t[2][before+1]
            ans = min(ans, d)
print(ans)