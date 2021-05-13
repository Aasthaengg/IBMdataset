n,m,q = map(int, input().split())
lr=[list(map(int,input().split())) for i in range(m)]
pq=[list(map(int,input().split())) for i in range(q)]
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
for l,r in lr:
    arr[l][r]+=1
rui = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        rui[i][j] = rui[i-1][j] + rui[i][j-1] - rui[i-1][j-1] + arr[i][j]

for p,q in pq:
    cnt = rui[q][q] - rui[p-1][q] - rui[q][p-1] + rui[p-1][p-1]
    print(cnt)