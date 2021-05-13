n,m,q = map(int,input().split())
trains = [[0]*(n+1) for _ in range(n+1)]
ans = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    l,r = map(int,input().split())
    trains[l][r] += 1
for i in range(1,n+1):
    cur = 0
    for j in range(i,n+1):
        cur += trains[i][j]
        ans[i][j] = cur
for i in range(q):
    p,q = map(int,input().split())
    ansi = 0
    for j in range(p,q+1):
        ansi += ans[j][q]
    print(ansi)