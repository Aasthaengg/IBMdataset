N = int(input())

P = []

for i in range(N):
    x,y = map(int,input().split())
    P.append((x,y))

mp = {}

for i in range(N):
    for j in range(i+1,N):
        mp[(P[i][0]-P[j][0],P[i][1]-P[j][1])] = 0
        mp[(P[j][0]-P[i][0],P[j][1]-P[i][1])] = 0

for i in range(N):
    for j in range(i+1,N):
        mp[(P[i][0]-P[j][0],P[i][1]-P[j][1])] += 1
        mp[(P[j][0]-P[i][0],P[j][1]-P[i][1])] += 1

ans = N
for i in mp:
    ans = min(ans,N-mp[i])

print(ans)