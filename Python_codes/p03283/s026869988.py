n , m , q = map(int, input().split())
table = [[0]*n for i in range(n)]

for i in range(m):
    l , r = map(int, input().split())
    l-=1
    r-=1
    table[l][r]+=1

table_sum = table.copy()

for i in range(n):
    for j in range(1,n):
        table_sum[i][j]=table_sum[i][j]+table_sum[i][j-1]

for i in range(q):
    l , r = map(int, input().split())
    l-=1
    r-=1
    ans=0
    for j in range(l,r+1):
        if l!=0:
            ans+=table_sum[j][r]-table_sum[j][l-1]
        else:
            ans+=table_sum[j][r]
    print(ans)
