N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

d = [[A[i][j] for i in range(N)]for j in range(N)]

for k in range(N):#wwa-ssyarru
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])

for i in range(N):#言われた通りに直でつなげるだけで最短炉更新されたらもう無理
    for j in range(N):
        if A[i][j]!=d[i][j]:
            print(-1)
            exit()

ans = 0
#経由で=のとこ合ったらそこはつかわない
for i in range(N):
    for j in range(N):
        ok = True
        for k in range(N):
            if k == i or k == j:
                continue
            if d[i][j]==d[i][k]+d[j][k]:
                ok=False
        if ok:
            ans+=d[i][j]

print(ans//2)
