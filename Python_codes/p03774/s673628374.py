N,M = map(int,input().split())
lsab = []
for i in range(N):
    a,b = map(int,input().split())
    lsab.append([a,b])
lscd = []
for j in range(M):
    c,d= map(int,input().split())
    lscd.append([c,d])

lsans = []
for i in range(N):
    max1 = 4*10**8+100
    ans = 0
    for j in range(M):
        dis = abs(lsab[i][0]-lscd[j][0])+abs(lsab[i][1]-lscd[j][1])
        if dis < max1:
            ans = j+1
            max1 = dis
    lsans.append(ans)

for i in range(N):
    print(lsans[i])