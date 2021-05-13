W,H,N = map(int,input().split())
ls = []
for i in range(N):
    ls.append(list(map(int,input().split())))
sur = [[1]*W for i in range(H)]
for i in range(N):
    if ls[i][2] == 1:
        for j in range(W):
            for k in range(H):
                if j < ls[i][0]:
                    sur[k][j] = 0
    if ls[i][2] == 2:
        for j in range(W):
            for k in range(H):
                if j >= ls[i][0]:
                    sur[k][j] = 0
    if ls[i][2] == 3:
        for j in range(W):
            for k in range(H):
                if k < ls[i][1]:
                    sur[k][j] = 0
    if ls[i][2] == 4:
        for j in range(W):
            for k in range(H):
                if k >= ls[i][1]:
                    sur[k][j] = 0
ans = 0
for i in range(H):
    ans += sur[i].count(1)
print(ans)