n,C = map(int,input().split())
d = [[int(i) for i in input().split()] for _ in range(C)]
c = [[int(i)-1 for i in input().split()] for _ in range(n)]

cnt = [[0]*C for _ in range(3)]
for i in range(n):
    for j in range(n):
        for k in range(C):
            cnt[(i+j)%3][k] += d[c[i][j]][k]

ans = float("inf")
for i in range(C):
    for j in range(C):
        if i == j: continue
        for k in range(C):
            if i == k or j == k: continue
            ans = min(ans, cnt[0][i] + cnt[1][j] + cnt[2][k])
print(ans)