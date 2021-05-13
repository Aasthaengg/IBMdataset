n,m,q = map(int,input().split())
l = [[0]*(n) for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    l[a-1][b-1] += 1


for i in range(n):
    for j in range(n):
        if i != 0:
            l[i][j] += l[i-1][j]
        if j != 0:
            l[i][j] += l[i][j-1]
        if i!= 0 and j != 0:
            l[i][j] -= l[i-1][j-1]
    

for i in range(q):
    a,b = map(int,input().split())
    ans = l[b-1][b-1]
    if a >= 2:
        ans -= l[a-2][b-1]
    print(ans)