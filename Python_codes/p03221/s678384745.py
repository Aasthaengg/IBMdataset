N,M = map(int,input().split())
PY = [list(map(int,input().split())) for i in range(M)]

ans = [[0,0]]*(M)

prefectures = [[] for i in range(0,N+1,1)]
for i in range(M):
    prefectures[PY[i][0]].append([PY[i][1],i])
for i in range(N+1):
    prefectures[i].sort()
for i in range(N+1):
    for j in range(len(prefectures[i])):
        ans[prefectures[i][j][1]]=[i,j+1]

for i in range(M):
    ans[i][0] = str(ans[i][0]).zfill(6)
    ans[i][1] = str(ans[i][1]).zfill(6)
    print("".join(ans[i]))

