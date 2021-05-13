n,m,q = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(m)]
query = [list(map(int,input().split())) for _ in range(q)]
s = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    l,r = lst[i]
    s[l][r] += 1

for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j] += s[i][j-1]

for i in range(q):
    l,r = query[i]
    ans = 0
    for j in range(l,r+1):
        ans += s[j][r] - s[j][l-1]
    print(ans)