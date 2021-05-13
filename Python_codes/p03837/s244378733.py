N,M = map(int, input().split())
inf = 10**8
d = [[inf]*N for _ in range(N)]
E = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
    E[a-1].append((b-1, c))

for i in range(N):
    d[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

cnt = 0
for i in range(N):
    for e in E[i]:
        j = e[0]
        c = e[1]
        flag = False
        for k in range(N):
            for l in range(k+1, N):
                if d[k][l] == d[k][i]+c+d[j][l] or d[k][l] == d[k][j]+c+d[i][l]:
                    cnt += 1
                    flag = True
                    break
            if flag:
                break
print(M-cnt)