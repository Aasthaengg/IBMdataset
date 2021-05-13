N,C = map(int,input().split())
D = [list(map(int,input().split())) for i in range(C)]
CS = [list(map(int,input().split())) for i in range(N)]

from collections import Counter
cs = [Counter() for _ in range(3)]
for i,row in enumerate(CS):
    for j,c in enumerate(row):
        cs[(i+j)%3][c-1] += 1

ans = float('inf')
for i in range(C):
    d1 = 0
    for c,v in cs[0].items():
        d1 += D[c][i]*v
    for j in range(C):
        if i==j: continue
        d2 = 0
        for c,v in cs[1].items():
            d2 += D[c][j]*v
        for k in range(C):
            if k==i or k==j: continue
            d3 = 0
            for c,v in cs[2].items():
                d3 += D[c][k]*v
            ans = min(ans, d1+d2+d3)
print(ans)