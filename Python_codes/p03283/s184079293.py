




N,M,Q = map(int, input().split())


trains = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    l,r = map(int, input().split())
    trains[l-1][r-1] += 1
    
query = [tuple(map(int, input().split())) for _ in range(Q)]



accum = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        if i == j:
            accum[i][j] = trains[i][j]
        else:
            accum[i][j] = accum[i][j-1] + trains[i][j]

for p, q in query:
    cnt = 0
    for i in range(p-1, q):
        cnt += accum[i][q-1]

    print(cnt)

