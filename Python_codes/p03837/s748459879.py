
N,M = map(int,input().split())
lis = [[float("inf")] * N for i in range(N)]
flis = [[False] * N for i in range(N)]
ans = 0

for i in range(N):
    lis[i][i] = 0

for i in range(M):

    a,b,c = map(int,input().split())

    a -= 1
    b -= 1

    lis[a][b] = c
    lis[b][a] = c

    flis[a][b] = True
    flis[b][a] = True

for k in range(N):

    for i in range(N):

        for j in range(N):

            if lis[i][j] > lis[i][k] + lis[k][j]:
                lis[i][j] = lis[i][k] + lis[k][j]

                if flis[i][j]:
                    flis[i][j] = False
                    flis[j][i] = False
                    ans += 1

print (ans)
