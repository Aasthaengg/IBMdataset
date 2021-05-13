N,C=map(int, input().split())
D=[list(map(int, input().split())) for _ in range(C)]
c=[list(map(int, input().split())) for _ in range(N)]

d = [[] for _ in range(3)]

for color in range(1,C+1):
    t = [0]*3
    for i in range(N):
        for j in range(N):
            if c[i][j] != color:
                t[(i+j)%3] += D[c[i][j]-1][color-1]
    for k in range(3):
        d[k].append((color, t[k]))

for k in range(3):
    d[k].sort(key=lambda x:x[1])

ans = 10**9
for i in range(3):
    for j in range(3):
        for k in range(3):
            if len({d[0][i][0], d[1][j][0], d[2][k][0]}) != 3: continue
            ans = min(ans, d[0][i][1] + d[1][j][1] + d[2][k][1])
print(ans)