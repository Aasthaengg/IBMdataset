N,W = map(int, input().split(' '))
A = [list(map(int, input().split(' '))) for i in range(N)]
if A[0][0] > 300:
    if W//A[0][0] > 100:
        print(sum(list(zip(*A))[1]))
        exit()
    if W%A[0][0] >= 300:
        W = W//A[0][0]*300+299
    else:
        W = W//A[0][0]*300+W%A[0][0]
    k = A[0][0]
    for i in range(N):
        A[i][0] = 300+A[i][0]-k

DP = [[0 for i in range(31000)] for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,31000):
        DP[i][j] = max(DP[i][j],DP[i-1][j],DP[i][j-1])
        if j-A[i-1][0]>=0:
            DP[i][j] = max(DP[i][j],DP[i-1][j-A[i-1][0]]+A[i-1][1])            

print(DP[N][W])
