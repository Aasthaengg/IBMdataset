N, M = map(int,input().split())

ab = []
for i in range(N):
    ab.append(list(map(int,input().split())))

cd = []
for i in range(M):
    cd.append(list(map(int,input().split())))

ans = [0 for i in range(N)]
for i in range(N):
    d = 1000000000
    for j in range(M):
        if d > abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1]):
            ans[i] = j+1
            d = abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1])

for i in range(N):
    print(ans[i])