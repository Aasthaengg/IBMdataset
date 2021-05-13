n,m = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(n)]
di = [list(map(int,input().split())) for _ in range(m)]
mn = [float("inf")]*n
num = [0]*n
for i in range(n):
    for j in range(m):
        k = abs(ls[i][0]-di[j][0]) + abs(ls[i][1]-di[j][1])
        if k < mn[i]:
            mn[i] = k
            num[i] = j+1
for p in range(n):
    print(num[p])
