N,M = map(int,input().split())
road = [[10**6]*N for i in range(N)]
tmp = []
for i in range(M):
    a,b,c = map(int,input().split())
    road[a-1][b-1] = c
    road[b-1][a-1] = c
    tmp.append([a-1,b-1,c])

for k in range(N):
   for i in range(N):
       for j in range(N):
           road[i][j] = min(road[i][j],road[i][k] + road[k][j]) 
ans = 0
for a,b,c in tmp:
    if road[a][b] != c:
        ans += 1

print(ans)
