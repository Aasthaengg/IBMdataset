n,m,q = map(int, input().split())
lr=[list(map(int,input().split())) for i in range(m)]
pq=[list(map(int,input().split())) for i in range(q)]
arr = [[0 for _ in range(n)] for _ in range(n)]
for l,r in lr:
    arr[l-1][r-1]+=1
rui = [[0 for _ in range(n)] for _ in range(n)]

rui[0][0] = arr[0][0]

for i in range(1,n):
    rui[i][0] = rui[i-1][0] + arr[i][0]
for j in range(1,n):
    rui[0][j] = rui[0][j-1] + arr[0][j]

for i in range(1,n):
    for j in range(1,n):
        rui[i][j] = rui[i-1][j] + rui[i][j-1] - rui[i-1][j-1] + arr[i][j]

for p,q in pq:
    p-=1
    q-=1
    cnt = rui[q][q]
    if p!=0:
        cnt-=rui[p-1][q]
        cnt-=rui[q][p-1]
        cnt+=rui[p-1][p-1]

    print(cnt)